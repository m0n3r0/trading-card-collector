# 5. Sealed Product

> **Act I — The hobby · chapter 5 of 12.** The cards you can buy (3 of 3). Sealed boxes: a different asset with
> its own risks (reseals, storage, reprint waves).

## 5.1 Product types

| Product | What it is | Notes |
|---------|-----------|-------|
| Booster pack | Single randomized pack | Easy to search (weigh, bend, light); loose packs from untrusted sellers are suspect |
| Booster box / display | 18-36 packs, factory sealed | The standard "sealed investment" unit |
| Case | Multiple boxes in manufacturer packaging | Case-fresh provenance is the best protection against tampering |
| ETB / collection boxes | Pokemon Elite Trainer Box, premium collections | Mass-market; Pokemon Center exclusives carry a premium |
| Hobby / jumbo / blaster / hanger | Sports formats | Hobby boxes hold guaranteed hits; retail does not |
| Starter / structure decks, bundles | Fixed contents | Low upside unless out-of-print and iconic |

## 5.2 Why sealed appreciates (when it does)

- Supply only shrinks after print ends: every opened box removes one.
- Openers (breakers, content creators) need sealed product, creating demand
  independent of collectors.
- Vintage sealed is often the only way to get a chance at a "pack fresh" 10.

## 5.3 Why it often does not


Why sealed can appreciate — and why it often doesn't.

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
  S["**Sealed product**"]:::key
  S --> UP["**Why it can appreciate**"]:::verify
  S --> DN["**Why it often doesn't**"]:::risk
  UP --> U1["supply shrinks — every opened box removes one"]:::verify
  UP --> U2["openers/breakers need it (demand independent of collectors)"]:::verify
  UP --> U3["vintage sealed = the only 'pack fresh' 10 chance"]:::verify
  DN --> D1["print waves: modern sets reprint until demand met"]:::risk
  DN --> D2["reprints of the set or its key cards cap upside"]:::risk
  DN --> D3["storage cost + damage risk, shrink tears"]:::risk
  DN --> D4["capital tied up for years; poor vs fees/inflation"]:::risk
```

- Print waves: modern sets are reprinted until demand is met.
- Reprints of a set or of its key cards in a new set cap upside.
- Storage cost and damage risk, shrink tears, crushed corners.
- Capital is tied up for years; returns versus fees and inflation are often
  poor except for the few iconic sets.

## 5.4 Reseal and tamper detection


The reseal-detection decision path.

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
  START["**Buying sealed**"]:::key --> A
  A{"Case-fresh from an<br/>authorized source?"}:::flow
  A -->|"yes"| A1["ask for case cards,<br/>invoices, distributor tape"]:::verify
  A -->|"no"| A2["compare wrap vs known genuine:<br/>seam, fold, logo, tightness"]:::unv
  A2 --> B
  A1 --> B{"Check flaps, glue,<br/>foil crimps, pack art<br/>for the print run"}:::flow
  B --> C{"Very expensive<br/>vintage sealed?"}:::key
  C -->|"yes"| C1["use third-party<br/>authentication + encapsulation"]:::verify
  C -->|"no"| DONE["**Accept / walk**"]:::endg
```

1. Buy case-fresh from authorized distributors or reputable shops where
   possible; ask for case cards, invoices, distributor tape.
2. Compare wrap with known genuine examples: seam pattern, fold style, logo
   printed on the wrap (many manufacturers use branded shrink), tightness.
3. Check box flaps and glue, foil pack crimps (vertical vs horizontal crimp,
   width), pack art versions for the print run.
4. Weighing packs (to find heavier hit packs) is a known practice in some
   products; avoid buying loose packs from sources that had the chance.
5. For very expensive vintage sealed, use third-party authentication and
   encapsulation (e.g. graders/authenticators offering sealed-product services;
   check which ones are accepted for the product you buy).

## 5.5 Storage

- Same environment as graded cards: cool, dark, stable, about 40-50% relative
  humidity, off the floor, away from exterior walls.
- Acrylic cases for high-value boxes; UV-protective acrylic for display.
- Keep cases sealed if you have them; photograph serials and labels.
- Record purchase price, date, source and photos in your records and log
  market sightings in the tracker (grader `RAW`, grade `sealed`).
