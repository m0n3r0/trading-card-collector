#!/usr/bin/env python3
"""
tracker.py -- own-data PSA 10 price tracker. No third-party APIs, no accounts,
no tokens. You log the prices you observe (sold listings, auction results,
shop/show sightings) and the tracker stores them, computes statistics, draws
its own charts, and flags buy signals against your targets.

Data lives in a local SQLite file (history.db next to this script by default).
Everything runs on the standard library.

Usage:
    python3 tracker.py add "Charizard #4 Base" --set "Base Set" --target 9000
    python3 tracker.py list
    python3 tracker.py record "Charizard #4 Base" 8750 --date 2026-09-28 \\
        --source "eBay sold" --url "https://..." --note "old cert, weak centering"
    python3 tracker.py sight "Charizard #4 Base" 9500 --source "LCS" --note "firm"
    python3 tracker.py history "Charizard #4 Base"
    python3 tracker.py chart "Charizard #4 Base" --kind sold
    python3 tracker.py chart "Charizard #4 Base" --html chart.html
    python3 tracker.py report
    python3 tracker.py alerts
    python3 tracker.py export --csv comps.csv
    python3 tracker.py selftest

A buy signal fires when the cheapest recent listing or the median of recent
sold comps sits at or under your target.
"""
import argparse
import datetime
import html
import json
import os
import sqlite3
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(HERE, "history.db")
KINDS = ("sold", "listing")
RECENT_DAYS = 90


# --------------------------------------------------------------------------
# storage
# --------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    set_name TEXT DEFAULT '',
    grade TEXT DEFAULT '10',
    grader TEXT DEFAULT 'PSA',
    target_usd REAL,
    note TEXT DEFAULT '',
    created TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY,
    card_id INTEGER NOT NULL REFERENCES cards(id),
    kind TEXT NOT NULL,
    price_usd REAL NOT NULL,
    ts TEXT NOT NULL,
    source TEXT DEFAULT '',
    url TEXT DEFAULT '',
    note TEXT DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_obs_card_ts ON observations(card_id, ts);
"""


def connect(db_path):
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)
    return con


def get_card(con, label):
    row = con.execute("SELECT * FROM cards WHERE label = ?", (label,)).fetchone()
    if row is None:
        raise SystemExit("unknown card: %r (see: list)" % label)
    cols = [d[0] for d in con.execute("SELECT * FROM cards LIMIT 0").description]
    return dict(zip(cols, row))


def today_iso():
    return datetime.date.today().isoformat()


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def cmd_add(con, a):
    try:
        con.execute(
            "INSERT INTO cards (label, set_name, grade, grader, target_usd, note, created)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (a.label, a.set or "", a.grade, a.grader, a.target,
             a.note or "", today_iso()),
        )
        con.commit()
    except sqlite3.IntegrityError:
        raise SystemExit("card already tracked: %r" % a.label)
    print("tracking %r (target %s)" % (a.label, fmt_usd(a.target)))


def cmd_list(con, _a):
    rows = con.execute(
        "SELECT label, set_name, grader, grade, target_usd FROM cards ORDER BY label"
    ).fetchall()
    if not rows:
        print("watchlist is empty (see: add)")
        return
    print("%-40s %-22s %-6s %12s" % ("LABEL", "SET", "GRADE", "TARGET"))
    for label, set_name, grader, grade, target in rows:
        print("%-40s %-22s %-6s %12s" % (
            label[:40], (set_name or "")[:22],
            ("%s %s" % (grader, grade))[:6], fmt_usd(target)))


def cmd_remove(con, a):
    card = get_card(con, a.label)
    con.execute("DELETE FROM observations WHERE card_id = ?", (card["id"],))
    con.execute("DELETE FROM cards WHERE id = ?", (card["id"],))
    con.commit()
    print("removed %r and its observations" % a.label)


def cmd_log(con, a, kind):
    card = get_card(con, a.label)
    if a.price <= 0:
        raise SystemExit("price must be positive")
    ts = a.date or today_iso()
    datetime.date.fromisoformat(ts)  # validates YYYY-MM-DD
    con.execute(
        "INSERT INTO observations (card_id, kind, price_usd, ts, source, url, note)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        (card["id"], kind, a.price, ts, a.source or "", a.url or "",
         a.note or ""),
    )
    con.commit()
    print("logged %s %s on %s from %s" % (
        kind, fmt_usd(a.price), ts, a.source or "unspecified"))


def observations(con, card_id, kind=None, since=None):
    q = "SELECT kind, price_usd, ts, source, url, note FROM observations WHERE card_id = ?"
    params = [card_id]
    if kind:
        q += " AND kind = ?"
        params.append(kind)
    if since:
        q += " AND ts >= ?"
        params.append(since)
    q += " ORDER BY ts"
    return [dict(zip(("kind", "price", "ts", "source", "url", "note"), r))
            for r in con.execute(q, params).fetchall()]


def stats(prices):
    if not prices:
        return None
    out = {"n": len(prices), "min": min(prices), "max": max(prices),
           "median": statistics.median(prices)}
    out["mean"] = statistics.fmean(prices)
    out["stdev"] = statistics.stdev(prices) if len(prices) > 1 else 0.0
    return out


def cmd_history(con, a):
    card = get_card(con, a.label)
    obs = observations(con, card["id"], kind=a.kind)
    if not obs:
        print("no observations for %r" % a.label)
        return
    print("%-6s %12s %-12s %-20s %s" % ("KIND", "PRICE", "DATE", "SOURCE", "NOTE"))
    for o in obs:
        print("%-6s %12s %-12s %-20s %s" % (
            o["kind"], fmt_usd(o["price"]), o["ts"],
            (o["source"] or "")[:20], (o["note"] or "")))
    s = stats([o["price"] for o in obs])
    print("n=%d median=%s mean=%s min=%s max=%s" % (
        s["n"], fmt_usd(s["median"]), fmt_usd(s["mean"]),
        fmt_usd(s["min"]), fmt_usd(s["max"])))


# --------------------------------------------------------------------------
# own charting: ASCII + standalone SVG (no libraries, no network)
# --------------------------------------------------------------------------

def ascii_chart(points, width=64, height=14):
    """points: [(ts, price)]. Returns a text chart string."""
    if not points:
        return "(no data)"
    prices = [p for _, p in points]
    lo, hi = min(prices), max(prices)
    span = (hi - lo) or 1.0
    cols = _resample(points, width)
    rows = []
    for r in range(height):
        level = hi - span * r / (height - 1)
        line = "".join("*" if v is not None and v >= level else " "
                       for _, v in cols)
        rows.append("%10s |%s" % (fmt_usd_short(level), line))
    axis = " " * 11 + "+" + "-" * width
    first_ts = cols[0][0] if cols[0][1] is not None else ""
    last_ts = next((t for t, v in reversed(cols) if v is not None), "")
    foot = " " * 11 + first_ts + " " * max(1, width - len(first_ts) - len(last_ts)) + last_ts
    return "\n".join(rows + [axis, foot])


def _resample(points, width):
    """Bucket points into `width` time columns, averaging each bucket."""
    t0 = points[0][0]
    t1 = points[-1][0]
    if t0 == t1:
        return [(t0, statistics.fmean([p for _, p in points]))]
    buckets = [[] for _ in range(width)]
    d0 = datetime.date.fromisoformat(t0).toordinal()
    d1 = datetime.date.fromisoformat(t1).toordinal()
    for ts, price in points:
        i = (datetime.date.fromisoformat(ts).toordinal() - d0) * (width - 1) // (d1 - d0)
        buckets[i].append(price)
    out = []
    for i, b in enumerate(buckets):
        frac = d0 + (d1 - d0) * i // max(1, width - 1)
        ts = datetime.date.fromordinal(frac).isoformat()
        out.append((ts, statistics.fmean(b) if b else None))
    return out


def svg_chart(label, points, target=None, width=760, height=320):
    """Standalone SVG line chart string. No JavaScript, no external assets."""
    pad_l, pad_r, pad_t, pad_b = 70, 16, 28, 34
    iw, ih = width - pad_l - pad_r, height - pad_t - pad_b
    prices = [p for _, p in points]
    lo = min(prices + ([target] if target else []))
    hi = max(prices + ([target] if target else []))
    span = (hi - lo) or 1.0
    lo -= span * 0.08
    hi += span * 0.08
    span = hi - lo

    def x(i):
        return pad_l + iw * i / max(1, len(points) - 1)

    def y(v):
        return pad_t + ih * (1 - (v - lo) / span)

    pts = " ".join("%.1f,%.1f" % (x(i), y(p)) for i, (_, p) in enumerate(points))
    grid = []
    for g in range(5):
        v = lo + span * g / 4
        gy = y(v)
        grid.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#ddd"/>'
                    % (pad_l, gy, pad_l + iw, gy))
        grid.append('<text x="%d" y="%.1f" font-size="11" fill="#555" text-anchor="end">%s</text>'
                    % (pad_l - 6, gy + 4, html.escape(fmt_usd_short(v))))
    target_line = ""
    if target:
        ty = y(target)
        target_line = (
            '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#c00"'
            ' stroke-dasharray="6,4"/>' % (pad_l, ty, pad_l + iw, ty)
            + '<text x="%d" y="%.1f" font-size="11" fill="#c00">target %s</text>'
            % (pad_l + iw, ty - 6, html.escape(fmt_usd(target))))
    dots = "".join(
        '<circle cx="%.1f" cy="%.1f" r="3" fill="#147"/>'
        '<title>%s %s</title>' % (x(i), y(p), ts, fmt_usd(p))
        for i, (ts, p) in enumerate(points))
    first, last = points[0][0], points[-1][0]
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">'
        '<rect width="100%%" height="100%%" fill="#fff"/>'
        '<text x="%d" y="18" font-size="14" font-family="sans-serif">%s</text>'
        '%s<polyline points="%s" fill="none" stroke="#147" stroke-width="2"/>%s%s'
        '<text x="%d" y="%d" font-size="11" fill="#555">%s</text>'
        '<text x="%d" y="%d" font-size="11" fill="#555" text-anchor="end">%s</text>'
        '</svg>' % (
            width, height, pad_l, html.escape(label), "".join(grid), pts,
            dots, target_line, pad_l, height - 10, html.escape(first),
            pad_l + iw, height - 10, html.escape(last)))


def svg_page(label, points, target):
    return ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<title>%s price history</title></head>"
            "<body style='font-family:sans-serif'>%s"
            "<p>n=%d, range %s to %s. Generated locally by tracker.py; no third parties involved.</p>"
            "</body></html>"
            % (html.escape(label), svg_chart(label, points, target), len(points),
               fmt_usd(min(p for _, p in points)), fmt_usd(max(p for _, p in points))))


def cmd_chart(con, a):
    card = get_card(con, a.label)
    obs = observations(con, card["id"], kind=a.kind)
    if not obs:
        print("no %s observations for %r" % (a.kind, a.label))
        return
    points = [(o["ts"], o["price"]) for o in obs]
    if a.html:
        with open(a.html, "w", encoding="utf-8") as f:
            f.write(svg_page("%s (%s)" % (card["label"], a.kind),
                             points, card["target_usd"]))
        print("wrote %s" % a.html)
    else:
        print("%s (%s), n=%d" % (card["label"], a.kind, len(points)))
        print(ascii_chart(points, width=a.width))


# --------------------------------------------------------------------------
# report + alerts
# --------------------------------------------------------------------------

def card_summary(con, card):
    cutoff = (datetime.date.today()
              - datetime.timedelta(days=RECENT_DAYS)).isoformat()
    sold = [o["price"] for o in observations(con, card["id"], "sold", since=cutoff)]
    listings = observations(con, card["id"], "listing", since=cutoff)
    cheap = min((o["price"] for o in listings), default=None)
    med = statistics.median(sold) if sold else None
    target = card["target_usd"]
    signal = "WATCH"
    if target:
        if (cheap is not None and cheap <= target) or \
           (med is not None and med <= target):
            signal = "BUY"
        elif (cheap is not None and cheap <= target * 1.10) or \
             (med is not None and med <= target * 1.10):
            signal = "NEAR"
    return {"sold_n": len(sold), "sold_median": med,
            "cheapest_listing": cheap, "signal": signal}


def fmt_usd(v):
    return "-" if v is None else "$%s" % format(v, ",.0f")


def fmt_usd_short(v):
    if v is None:
        return "-"
    if abs(v) >= 1000:
        return "$%.1fk" % (v / 1000)
    return "$%.0f" % v


def cmd_report(con, _a):
    cards = con.execute("SELECT * FROM cards ORDER BY label").fetchall()
    cols = [d[0] for d in con.execute("SELECT * FROM cards LIMIT 0").description]
    if not cards:
        print("watchlist is empty (see: add)")
        return
    print("%-36s %10s %6s %12s %12s %-5s" % (
        "CARD", "TARGET", "SOLD", "MED SOLD", "CHEAP LIST", "SIG"))
    for row in cards:
        card = dict(zip(cols, row))
        s = card_summary(con, card)
        print("%-36s %10s %6d %12s %12s %-5s" % (
            card["label"][:36], fmt_usd(card["target_usd"]), s["sold_n"],
            fmt_usd(s["sold_median"]), fmt_usd(s["cheapest_listing"]),
            s["signal"]))


def cmd_alerts(con, _a):
    cards = con.execute("SELECT * FROM cards ORDER BY label").fetchall()
    cols = [d[0] for d in con.execute("SELECT * FROM cards LIMIT 0").description]
    hits = [(dict(zip(cols, row)), card_summary(con, dict(zip(cols, row))))
            for row in cards]
    hits = [(c, s) for c, s in hits if s["signal"] == "BUY"]
    if not hits:
        print("no buy signals")
        return
    for card, s in hits:
        print("BUY %s: target %s, median sold %s, cheapest listing %s" % (
            card["label"], fmt_usd(card["target_usd"]),
            fmt_usd(s["sold_median"]), fmt_usd(s["cheapest_listing"])))


def cmd_export(con, a):
    import csv
    rows = con.execute(
        "SELECT c.label, o.kind, o.price_usd, o.ts, o.source, o.url, o.note"
        " FROM observations o JOIN cards c ON c.id = o.card_id"
        " ORDER BY c.label, o.ts").fetchall()
    with open(a.csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["label", "kind", "price_usd", "date", "source", "url", "note"])
        w.writerows(rows)
    print("wrote %d rows to %s" % (len(rows), a.csv))


def cmd_import(con, a):
    with open(a.json, encoding="utf-8") as f:
        entries = json.load(f)
    added, skipped = 0, 0
    for e in entries:
        try:
            con.execute(
                "INSERT INTO cards (label, set_name, grade, grader, target_usd,"
                " note, created) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (e["label"], e.get("set", ""), e.get("grade", "10"),
                 e.get("grader", "PSA"), e.get("target_usd"),
                 e.get("note", ""), today_iso()),
            )
            added += 1
        except (sqlite3.IntegrityError, KeyError):
            skipped += 1
    con.commit()
    print("imported %d cards, skipped %d" % (added, skipped))


# --------------------------------------------------------------------------
# offline selftest (no network, no user data)
# --------------------------------------------------------------------------

def cmd_selftest(_con, _a):
    con = sqlite3.connect(":memory:")
    con.executescript(SCHEMA)
    con.execute(
        "INSERT INTO cards (label, set_name, grade, grader, target_usd, note, created)"
        " VALUES ('Test Zard', 'Base Set', '10', 'PSA', 9000, '', '2026-01-01')")
    cid = con.execute("SELECT id FROM cards").fetchone()[0]
    d = datetime.date.today()
    fixtures = [(d - datetime.timedelta(days=80), 9500),
                (d - datetime.timedelta(days=40), 9200),
                (d - datetime.timedelta(days=10), 8800)]
    for ts, price in fixtures:
        con.execute(
            "INSERT INTO observations (card_id, kind, price_usd, ts)"
            " VALUES (?, 'sold', ?, ?)", (cid, price, ts.isoformat()))
    con.execute(
        "INSERT INTO observations (card_id, kind, price_usd, ts, source)"
        " VALUES (?, 'listing', 8900, ?, 'LCS')",
        (cid, (d - datetime.timedelta(days=5)).isoformat()))
    card = get_card(con, "Test Zard")
    assert card["target_usd"] == 9000
    sold = observations(con, cid, "sold")
    assert [o["price"] for o in sold] == [9500, 9200, 8800]
    assert stats([9500, 9200, 8800])["median"] == 9200
    s = card_summary(con, card)
    assert s["signal"] == "BUY", s  # 8900 listing under 9000 target
    text = ascii_chart([(o["ts"], o["price"]) for o in sold], width=20)
    assert "*" in text and fixtures[0][0].isoformat() in text \
        and fixtures[-1][0].isoformat() in text
    page = svg_page("Test Zard (sold)",
                    [(o["ts"], o["price"]) for o in sold], 9000)
    assert "<svg" in page and "http" not in page.replace("http://www.w3.org", "")
    assert "javascript" not in page.lower()
    print("SELFTEST OK (sqlite, stats, signals, ascii chart, standalone svg)")


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(description="Own-data PSA 10 price tracker.")
    p.add_argument("--db", default=DEFAULT_DB, help="sqlite file (default history.db)")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="track a card")
    a.add_argument("label")
    a.add_argument("--set", default="")
    a.add_argument("--grade", default="10")
    a.add_argument("--grader", default="PSA")
    a.add_argument("--target", type=float, default=None,
                   help="buy-at-or-under price in USD")
    a.add_argument("--note", default="")

    sub.add_parser("list", help="show watchlist")
    r = sub.add_parser("remove", help="untrack a card and its data")
    r.add_argument("label")

    for name, kind in (("record", "sold"), ("sight", "listing")):
        c = sub.add_parser(name, help="log a %s observation" % kind)
        c.add_argument("label")
        c.add_argument("price", type=float)
        c.add_argument("--date", default=None, help="YYYY-MM-DD (default today)")
        c.add_argument("--source", default="")
        c.add_argument("--url", default="")
        c.add_argument("--note", default="")

    h = sub.add_parser("history", help="show logged observations")
    h.add_argument("label")
    h.add_argument("--kind", choices=list(KINDS) + ["all"], default="all")

    c = sub.add_parser("chart", help="draw the price history")
    c.add_argument("label")
    c.add_argument("--kind", choices=list(KINDS), default="sold")
    c.add_argument("--width", type=int, default=64)
    c.add_argument("--html", default=None, help="write standalone page to file")

    sub.add_parser("report", help="watchlist vs targets")
    sub.add_parser("alerts", help="only buy signals")

    e = sub.add_parser("export", help="dump observations to csv")
    e.add_argument("--csv", required=True)

    i = sub.add_parser("import", help="load watchlist entries from a json file")
    i.add_argument("--json", required=True)

    sub.add_parser("selftest", help="offline checks, no network")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.cmd == "selftest":
        return cmd_selftest(None, args)
    con = connect(args.db)
    try:
        if args.cmd == "add":
            cmd_add(con, args)
        elif args.cmd == "list":
            cmd_list(con, args)
        elif args.cmd == "remove":
            cmd_remove(con, args)
        elif args.cmd in ("record", "sight"):
            cmd_log(con, args, "sold" if args.cmd == "record" else "listing")
        elif args.cmd == "history":
            if args.kind != "all":
                cmd_history(con, args)
            else:
                for k in KINDS:
                    args.kind = k
                    cmd_history(con, args)
        elif args.cmd == "chart":
            cmd_chart(con, args)
        elif args.cmd == "report":
            cmd_report(con, args)
        elif args.cmd == "alerts":
            cmd_alerts(con, args)
        elif args.cmd == "export":
            cmd_export(con, args)
        elif args.cmd == "import":
            cmd_import(con, args)
    finally:
        con.close()


if __name__ == "__main__":
    main()
