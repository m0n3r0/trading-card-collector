# Trading Cards: Collector and Buyer Handbook

This handbook covers the whole trading card hobby: sports cards and the main
collectible card games (TCGs). The Pokemon PSA 10 guide (`../psa10-guide.md`)
is the deep dive for one niche. These chapters cover the rest and are written
so the same buying discipline carries over to any card.

| # | Chapter | What it covers |
|---|---------|----------------|
| 1 | [market-overview.md](market-overview.md) | History from tobacco cards to the 2020s boom, how the industry is structured, who makes what, market cycles |
| 2 | [grading-companies.md](grading-companies.md) | PSA, BGS, SGC, CGC, TAG compared: scales, subgrades, labels, crossovers, and which grader to use for which card |
| 3 | [sports-cards.md](sports-cards.md) | Rookies, parallels, numbered cards, autos and relics, hobby vs. retail, case breaks, key vintage and modern cards |
| 4 | [tcg-collecting.md](tcg-collecting.md) | Magic, Yu-Gi-Oh!, One Piece, Lorcana, Digimon, Weiss Schwarz, Japanese Pokemon: rarity systems, reprint risk, language premiums |
| 5 | [sealed-product.md](sealed-product.md) | Booster boxes, ETBs, cases: holding sealed, reseal detection, storage |
| 6 | [fakes-and-scams.md](fakes-and-scams.md) | Counterfeit cards and slabs, trimming and alteration, marketplace and break scams |
| 7 | [valuation-and-selling.md](valuation-and-selling.md) | Building a fair value for any card, selling channels and fees, taxes and record keeping |
| 8 | [glossary.md](glossary.md) | Hobby vocabulary across sports cards and TCGs |
| 9 | [sources.md](sources.md) | Where the facts here came from, and when they were checked |

## How to use with the tracker

`../../tracker/tracker.py` is not limited to Pokemon. Each tracked card stores a
free-text grader and grade, so you can log a BGS 9.5 Luka Doncic Prizm, a CGC 10
Black Lotus or a raw sealed box in the same database:

```bash
python3 tracker.py add "Black Lotus Unlimited" --set "Unlimited" --grader BGS --grade 8 --target 20000
python3 tracker.py add "LOB 1st Ed Booster Box" --set "Legend of Blue Eyes" --grader RAW --grade sealed
```

## Ground rules used throughout

1. Price claims carry a date and a source. Anything older than about a year is
   history, not a quote.
2. Facts that could not be checked against a source say so.
3. No chapter is investment advice. Cards are illiquid, carry high fees and are
   driven by fashion. Buy what you would be happy to keep.
