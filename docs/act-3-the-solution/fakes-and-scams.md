# 6. Fakes, Alterations and Scams

> **Act III — The solution · chapter 14 of 16.** The shadows. Where the money actually goes wrong. The minimum defence
> here is what the guide's authentication section runs on.

## 6.1 Counterfeit raw cards

Checks (use several, never only one):

| Check | How | Catches |
|-------|-----|---------|
| Compare with a known genuine | Same set and print, side by side | Font, color saturation, holo pattern, border width |
| Loupe (30-60x) | Look at printed areas | Genuine offset printing shows a rosette dot pattern; many fakes show inkjet spray or flat color |
| Light test | Shine a phone light through the card | Card stock with an inner layer (black or blue core in MTG/Pokemon WOTC era) blocks more light; fakes may glow evenly |
| Feel and thickness | Calipers, flexibility | Fakes often feel glossy, thin or stiff |
| Weight | Gram scale vs. genuine | Rough screen only |
| Holo / foil | Tilt under light | Wrong holo pattern or holo where there should be none |
| Text and set symbols | Read every line | Typos, wrong copyright years, wrong set symbol |
| Edges | Look at the cut | Uneven or rough cuts |

High-risk cards: WOTC-era Pokemon holos (especially Charizard), Pokemon
Japanese promos, MTG Power Nine and dual lands (Alpha/Beta), Yu-Gi-Oh LOB 1st
Edition, sports rookies of superstars, any card trading above a few hundred
dollars.

## 6.2 Fake slabs and swapped cards


Fake-slab and card-swap detection, in order.

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
  SLAB["**A slab you're about to trust**"]:::key
  SLAB --> CERT["**Cert lookup**<br/>number must return THIS card,<br/>set, grade — else instant walk"]:::verify
  CERT --> VIS["**Slab inspection**<br/>crisp welds, sharp label, scannable<br/>barcode; rattle = compromised"]:::flow
  VIS --> CLONE{"**Cert cloning?**<br/>real number on a fake slab"}:::key
  CLONE -->|"match seller photos vs<br/>known slab-era traits"| ERA
  CLONE -->|"$1,000+"| AUTH["**insist on platform auth or<br/>auction-house provenance**"]:::verify
  ERA["**era check**"]:::flow --> SWAP
  AUTH --> SWAP{"**Card swap?**<br/>genuine slab, wrong card inside"}:::key
  SWAP -->|"visible defect in a '10'"| BAD["**it's a swap — walk**"]:::risk
  SWAP -->|"matches grade"| POST["**$1,000+ from a stranger:**<br/>post-purchase reholder/review"]:::verify
```

- Counterfeit slabs exist for PSA, BGS, SGC and CGC.
- Always verify the cert online and compare the database image (where
  provided) with the card in the slab: centering, print marks, holo flaws
  match on the real one.
- Check label printing, hologram, the slab seam, tamper evidence (cracks,
  glue, re-welded edges) and slab generation (older slab types should match the
  cert's era).
- If the card is worth the risk, crossover or reholder through the grader
  confirms authenticity.

## 6.3 Alterations

- Trimming: edges cut to sharpen corners. Check dimensions against standard
  size and edge texture; graded "Authentic"/"A" labels may indicate alteration.
- Recoloring: ink on edges/corners to hide whitening; look under angled light.
- Pressing/cleaning: removing dents or dirt. Policies differ by grader; some
  techniques are accepted, others count as alteration.
- Restoration of vintage: rebacking, fill. Usually only disclosed on high-end.

## 6.4 Marketplace scams

| Scam | Red flags | Defense |
|------|-----------|---------|
| Stock photos / wrong item | No photo of the actual card or slab | Ask for photos with your username and date |
| Off-platform payment | "Pay by friends and family, save fees" | Use platform checkout or goods-and-services payments with buyer protection |
| Account takeover | Old seller account suddenly selling grails cheaply | Check feedback history and recent category changes |
| Shill bidding | Bids from new or single-seller accounts | Set walk-away price; ignore bid war |
| Fake grails in social media groups | Price far below market, urgency | Use a trusted middleman or meet with verification |
| Break fraud | Pre-searched or swapped product, hidden case origins, disappearing hits | Use established breakers; watch full uncut video; check case sources |
| Return swap (for sellers) | Buyer returns a different/fake card | Record cert numbers, video packing, use non-returnable listings where allowed |
| Grading-submission middlemen | Holds cards for months, disappears | Submit directly or via long-established, reviewed services |

## 6.5 Minimum process for any card over your comfort limit


The minimum process, as a decision path with walk-away branches.

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
  C0["**Any card over your comfort limit**"]:::key
  C0 --> P1["**1. Price check**<br/>against SOLD comps, not asks"]:::act3
  P1 --> P2{"**2. Seller check**<br/>feedback, history, consistency"}:::flow
  P2 -->|"red flags"| WALK["**Walk away**"]:::risk
  P2 -->|"ok"| P3{"**3. Item check**<br/>cert verification, front/back,<br/>specific defects"}:::flow
  P3 -->|"mismatch"| WALK
  P3 -->|"ok"| P4["**4. Pay with buyer protection**<br/>never off-platform / friends&family"]:::act3
  P4 --> P5["**5. On arrival**<br/>unbox on video, re-verify cert,<br/>report in the dispute window"]:::act3
  P5 --> DONE["**Filed & safe**"]:::verify
```

1. Price check against sold comps (not asking prices).
2. Seller check: feedback, history, consistency.
3. Item check: cert verification, photos front and back, specific defects.
4. Payment with buyer protection.
5. On arrival: unbox on video, verify cert again, compare with photos, report
   problems inside the platform's dispute window.
