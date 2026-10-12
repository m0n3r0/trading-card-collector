# 7. Valuation and Selling

> **Act III — The solution · chapter 12 of 15.** The value. The method the deep dive runs on: fair value from *sold*
> comps, at least one source outside the grader's group, and a walk-away price. A
> prerequisite to the PSA 10 guide.

## 7.1 Building a fair value for any card


Building a fair value, step by step.

```mermaid

flowchart TD
classDef act1 fill:#dbeafe,stroke:#1e40af,stroke-width:2px,color:#1e3a8a;
classDef act2 fill:#fee2e2,stroke:#b91c1c,stroke-width:2px,color:#7f1d1d;
classDef act3 fill:#dcfce7,stroke:#15803d,stroke-width:2px,color:#14532d;
classDef key fill:#fde68a,stroke:#b45309,stroke-width:2.5px,color:#78350f;
classDef risk fill:#fecaca,stroke:#991b1b,stroke-width:2px,color:#7f1d1d;
classDef verify fill:#bbf7d0,stroke:#15803d,stroke-width:2px,color:#14532d;
classDef unv fill:#fef3c7,stroke:#b45309,stroke-width:2px,stroke-dasharray:6 4,color:#78350f;
classDef money fill:#fef9c3,stroke:#a16207,stroke-width:2px,color:#713f12;
classDef flow fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#334155;
classDef endg fill:#e2e8f0,stroke:#475569,stroke-width:2px,color:#1e293b;
  S1["**1. Identify the exact item**<br/>game, set, number, variant,<br/>grader, grade"]:::act3 --> S2
  S2["**2. Gather 30-90d sold comps**<br/>eBay sold, auction archives,<br/>APR, 130point, Cardmarket, tracker"]:::act3 --> S3
  S3["**3. Clean the data**<br/>drop best-offer ambiguity, damaged,<br/>shill outliers"]:::act3 --> S4
  S4["**4. Weight by recency & similarity**<br/>same grader/grade/eye-appeal;<br/>median beats last sale"]:::act3 --> S5
  S5["**5. Adjust for trend**<br/>30d vs 90d median; watch pop"]:::act3 --> S6
  S6["**6. Set walk-away = tracker target**"]:::verify
```

1. Identify the exact item: game/sport, set, number, variant (1st Ed,
   parallel, serial number, language), grader, grade.
2. Gather sold comps from the last 30-90 days:
   - eBay sold listings (filter "Sold items")
   - Auction house archives (Goldin, Heritage, PWCC/Fanatics Collect, REA)
   - PSA Auction Prices Realized, 130point, Card Ladder, PriceCharting.
     PSA APR is run by the grader, and Card Ladder is reported to belong to the
     same group (Collectors). Always include at least one source outside it,
     such as eBay sold, 130point, an auction archive or your tracker log
     (`../act-1-the-hobby/grading-companies.md` 2.7).
   - TCG-specific: TCGplayer market price (US), Cardmarket (EU), Japanese
     shops/marketplaces for Japanese prints
3. Clean the data: remove best-offer ambiguity (look up accepted offer when
   possible), damaged/autograph variants, shill-looking outliers.
4. Weight by recency and similarity: same grader, same grade, similar eye
   appeal. A median of recent sales beats the single last sale.
5. Adjust for trend: compare 30-day median with 90-day median; watch the
   population trend.
6. Set a walk-away price and log it as `--target` in the tracker.

## 7.2 Selling channels

| Channel | Best for | Costs (indicative, verify) | Notes |
|---------|----------|----------------------------|-------|
| eBay | Most cards | Final value fee in the low-teens percent, plus payment/shipping | Largest audience; authenticity guarantee program for high-value cards |
| TCGplayer / Cardmarket | Raw and graded TCG cards | Marketplace commission plus payment fees | Price-driven; expects accurate condition |
| Auction houses | High-end graded cards | Seller commission (negotiable at high value) plus buyer's premium on the buyer side | Wider reach for grails; consignment wait times |
| Whatnot and live apps | Mid-range, entertainment-led | Platform commission plus processing | Fast sales; prices depend on audience on the day |
| Card shows and shops | Quick cash, trades | Dealers pay roughly 60-85% of market | No fees, but lower price |
| Consignment / vault platforms | Hands-off selling | Commission plus storage/withdrawal fees | Check withdrawal rules before vaulting |
| Social media groups | Low fees | Trust risk | Use protected payment only |

Fee levels change; check the platform's fee page before listing.

## 7.3 Pricing your listing

- Fixed price at about the recent median for quick sales; slightly above with
  best offer for patience.
- Auctions work best for cards with deep demand; set a reserve or starting
  price you can live with.
- Show the cert number and full front/back photos; mention flaws.

## 7.4 Taxes and records (general, not tax advice)

- Many jurisdictions treat collectibles gains differently from stocks (for
  example, the US taxes collectibles at a special long-term rate up to 28%).
- Marketplaces issue reporting forms above thresholds that change by year and
  country.
- Keep for every card: purchase date, price, fees, grading costs, shipping,
  sale price, platform. The tracker's `export --csv` can hold your price
  history; keep cost basis records separately or in notes.
- Ask a tax professional in your country before selling at scale.
