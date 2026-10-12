# trading-card-collector

**One story: how a piece of cardboard becomes a tradeable asset — and how to buy a
PSA 10 Pokemon card without getting burned.**

This repository is a single story told across a few files. You do not need to read
them all at once, but read them in the order below and the whole hobby — and the
specific craft of buying a PSA 10 Pokemon card — comes together as one argument:
*the grade is what makes the card valuable, the people who assign the grade have
increasingly become the people who store, price and sell the card, and the only
defence is to understand the whole system and keep your own numbers independent.*

## The story in one breath

The trading-card hobby turns cheap cardboard into liquid, comparable assets by
**grading** it. A "10" on a slab is what lets a stranger trust a card's condition
without re-inspecting it, and that trust is what creates the price premium and the
resale liquidity. But that trust rests on a neutral referee — and the referee has
gotten a lot less neutral. PSA's parent, Collectors, now also owns the other two
major graders (BGS, SGC), runs a vault and instant-sale marketplace, and is reported
to own a price-data tool. When the grader is also the market, the number on the slab
is not as innocent as it looks. This repo walks you through that system end to end,
and then spends most of its energy on the one niche it exists for: **PSA 10
Pokemon** — how to read the grade, the population report, the price, the fakes, and
the transaction, and when it is actually worth grading your own card.

## Reading path — the story in nine moves

Read top to bottom. Each move is one or two chapters; the connective sentence tells
you why it matters to the story.

**I. The world** — how the hobby got here, and how the industry is built.
`docs/trading-cards/market-overview.md`
The history (tobacco cards → junk wax → the 2020 boom), the chain from IP licence to
grader, the three segments, and why markets boom and then correct. You cannot reason
about price without knowing what "price" is made of.

**II. The referees** — who grades the cards, and who really owns them.
`docs/trading-cards/grading-companies.md`
The five graders and what each grade means in practice — and the consolidation that
put PSA, BGS and SGC under one roof (Collectors). This is the turn of the story: the
neutral referee becomes a market participant.

**II.5. The eyewitnesses** — the evidence that motivates the playbook.
`docs/the-hobby-documentary-notes.md` ("The Hobby" film: the boom, grading as the
value engine, and how violently prices swing) and
`docs/psa-monopoly-video-notes.md` (the PSA/Collectors conflict-of-interest case:
reholder risk, upcharges, and why your price checks must come from outside the
group). Read these before the deep dive; they are *why* the guide's rules exist.

**III. The cards** — the three things you can actually buy.
`docs/trading-cards/sports-cards.md` (rookies, parallels, records),
`docs/trading-cards/tcg-collecting.md` (the card games — this is where Pokemon lives),
`docs/trading-cards/sealed-product.md` (sealed boxes, a different animal). You need
the vocabulary and the segment logic before you can value a specific card.

**IV. The value** — turning an opinion into a number you can act on.
`docs/trading-cards/valuation-and-selling.md`
Building a fair value from sold comps, the selling channels and their fees, and the
tax/record-keeping discipline. This is the method the Pokemon guide will keep
re-using, so the handbook's valuation chapter is a prerequisite to the deep dive.

**V. The shadows** — where the money actually goes wrong.
`docs/trading-cards/fakes-and-scams.md`
Counterfeit cards and slabs, trimming and alterations, and marketplace scams — plus
the minimum defence. Every purchase in the deep dive runs on the assumption that the
slab is real; this chapter is what makes that assumption safe.

**VI. The deep dive** — the niche this repo is about.
`docs/psa10-guide.md`
The complete PSA 10 Pokemon playbook: what the grade means precisely, population
reports, how PSA 10 prices behave, the grade-your-own-card math, buying online and
offline, authentication, condition traps inside the grade, paying/shipping/insurance,
storage, selling later, the expensive rookie mistakes, and the checklists. Everything
in moves I–V is applied here, Pokemon-specific.

**VII. The fix** — the grading issue, a deep dive, and a proposal for fairer rules.
`docs/trading-cards/fair-grading.md`
The special report: five verified parts of the problem (consolidation, the
referee-in-the-market structure, the 9-to-10 cliff — the same Pikachu Illustrator
sold for $16.5M as a PSA 10 and $1,406,250 as a PSA 9, five weeks apart in early
2026 — opaque supply, and an accountability gap), and a four-layer Fair Grading
Framework from structural separation to what you can do today. Read after the deep
dive; it turns the guide's rules into a standard and shows where the industry-side
fix is missing.

**VIII. The tool** — keeping your own data independent of the grader's group.
`tracker/` (see `tracker/README.md`)
Your own log of sold comps and listing sightings, with buy-signal alerts against your
targets and standalone ASCII/SVG charts. No third-party APIs, no accounts. It is the
one source in this repo that Collectors does not own — and the practical answer to
the conflict of interest raised in move II.

**Supporting chapters** (open whenever you need them, not in sequence):
`docs/trading-cards/glossary.md` — the hobby vocabulary, all in one place.
`docs/trading-cards/sources.md` — where the facts here come from and when they were
checked; it also indexes the two video sources.

## How the story hangs together

The whole repo is one argument with a spine:

1. **Grading creates the value.** A neutral, published, comparable grade is what
   turns cardboard into a liquid asset. (Move I–II; the documentary's "value engine.")
2. **The referee stopped being neutral.** PSA's owner now controls two more major
   graders, a vault, a marketplace, and (reportedly) a price tool. (Move II; the
   monopoly video; `grading-companies.md` 2.7.)
3. **So the buyer's job is to stay independent.** Build your fair value from sold
   comps that are not all from the grader's corporate group, keep at least one
   outside source in every price check, document the cert before and after every
   transaction, insure fully, and log your own comps in a tool the group cannot
   touch. (Moves IV–V, VII and VIII; `valuation-and-selling.md` 7.1; the guide's
   sections 3, 5, 8 and 11.)
4. **The fix has a long side and a short side.** The short side is the collector
   playbook you can run today (move VII, Layer 3). The long side is structural:
   separation of grading from market and price-data roles, published gem rates and
   subgrades, audited consistency, chain of custody, real liability — with the
   credit-rating industry's 2006 reform as the template for how a rating industry
   got reformed after its conflicts became obvious (move VII, Layers 1–2 and 4).

The Pokemon guide (VI) is the destination, the handbook chapters (I–V) are the
world it lives in, the fix report (VII) is the argument made explicit, the two
video notes are the eyewitnesses, and the tracker is the instrument. If you only
remember one sentence: **the grade is the product, but the number on the slab is
not the whole truth — your independent data is.**

## Ground rules used across every file

1. Price claims carry a date and a source. Anything older than about a year is
   history, not a quote — pull today's number from `tracker/`.
2. Facts that could not be checked against a source say so, in the text and in
   `docs/trading-cards/sources.md`.
3. No chapter is investment advice. Cards are illiquid, carry high fees, and are
   driven by fashion. Buy what you would be happy to keep.