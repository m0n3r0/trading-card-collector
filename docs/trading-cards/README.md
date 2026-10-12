# The Trading-Card Handbook — the world around the card

This is the context half of the repo's one story. The top-level [`README.md`](../../README.md)
tells the whole argument; these nine chapters are the *world* it lives in — the market,
the graders and who owns them, the three card segments, how to price and sell, and the
fakes that make the whole thing dangerous. Read them in order (I → V) and they build a
foundation the Pokemon deep dive ([`../psa10-guide.md`](../psa10-guide.md)) applies to one
specific card: the PSA 10.

The story so far: **grading is what makes a card valuable, but the graders are no longer
neutral.** These chapters set up that tension before the guide resolves it, Pokemon by
Pokemon.

## Chapters, in the order the story needs them

**I. [Market overview](market-overview.md)** — the hobby's history, the industry chain
from IP licence to grader, the three segments, and why markets boom and correct. Start
here: you cannot reason about price without knowing what price is made of.

**II. [Grading companies compared](grading-companies.md)** — the five graders, what each
grade means in practice, and the consolidation that put PSA, BGS and SGC under one owner
(Collectors). Section 2.7 is the turn of the story: the referee becomes a market
participant. This is what motivates every "use an independent price source" rule later.

**III. The three things you can actually buy.**
- [Sports cards](sports-cards.md) — rookies, parallels, serials, autos, and the records.
- [Collectible card games](tcg-collecting.md) — Pokemon, Magic, Yu-Gi-Oh!, One Piece,
  Lorcana and friends, plus the rules that apply to every TCG. **This is where Pokemon
  lives**; the deep dive assumes this vocabulary.
- [Sealed product](sealed-product.md) — booster boxes and ETBs: a different asset with
  its own risks (reseals, storage, reprint waves).

**IV. [Valuation and selling](valuation-and-selling.md)** — the method: build a fair value
from *sold* comps, keep at least one source outside the grader's corporate group, weigh
by recency, set a walk-away price. Then the selling channels and fees, and the tax and
record-keeping discipline. **This chapter is a prerequisite to the deep dive** — the guide
re-uses its rules for every PSA 10 purchase.

**V. [Fakes, alterations and scams](fakes-and-scams.md)** — counterfeit raw cards and slabs,
trimming and recoloring, and the marketplace scams. The minimum defence process here is
what the guide's authentication section runs on. Read it before you trust any slab.

## The fix (special report)

**[Fair grading: the problem, the evidence, and a proposal for collectors](fair-grading.md)** —
the grading issue as a deep dive: five verified parts of the problem (consolidation under
Collectors; the referee-in-the-market structure; the 9-to-10 cliff, with the same Pikachu
Illustrator selling for $16.5M as a PSA 10 and $1,406,250 as a PSA 9 in early 2026; opaque
gem-rate/pop supply; an accountability gap documented by BBB), and a four-layer **Fair
Grading Framework** — structural separation, transparency standards, market mechanisms you
can use today, and governance/advocacy. Every factual claim carries a source tag and a
verification appendix; reported-but-unverified claims are labelled as such. This is the
missing link between the grader chapters (II) and the deep dive (VI): the guide's rules
become a standard, and the industry-side fix is specified.

## Reference chapters (open whenever, not in sequence)

- [Glossary](glossary.md) — the hobby vocabulary across sports and TCGs. Terms already
  defined in the guide's own glossary ([`../psa10-guide.md`](../psa10-guide.md) §18) are
  not repeated here.
- [Sources](sources.md) — where the facts in these chapters come from and when they were
  checked, plus the two video sources behind the repo's evidence layer.

## Where the story goes next

- **The deep dive** — apply all of the above to the card this repo exists for:
  [`../psa10-guide.md`](../psa10-guide.md).
- **The eyewitnesses** — what the two documentaries actually said, and what we kept from
  them: [`../the-hobby-documentary-notes.md`](../the-hobby-documentary-notes.md) and
  [`../psa-monopoly-video-notes.md`](../psa-monopoly-video-notes.md).
- **The tool** — keep your own price data independent of the grader's group:
  [`../../tracker/`](../../tracker/README.md). `tracker.py` is not limited to Pokemon —
  each tracked card stores a free-text grader and grade, so you can log a BGS 9.5 Luka
  Doncic Prizm, a CGC 10 Black Lotus, or a raw sealed box in the same database:

  ```bash
  python3 ../../tracker/tracker.py add "Black Lotus Unlimited" --set "Unlimited" --grader BGS --grade 8 --target 20000
  python3 ../../tracker/tracker.py add "LOB 1st Ed Booster Box" --set "Legend of Blue Eyes" --grader RAW --grade sealed
  ```

## Ground rules used throughout

1. Price claims carry a date and a source. Anything older than about a year is history,
   not a quote.
2. Facts that could not be checked against a source say so, in the text and in
   [sources.md](sources.md).
3. No chapter is investment advice. Cards are illiquid, carry high fees, and are driven
   by fashion. Buy what you would be happy to keep.