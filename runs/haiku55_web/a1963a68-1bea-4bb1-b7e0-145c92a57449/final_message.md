I'll start by researching the Korean ride-hailing market as of May 2024: market share, regulation, driver supply, and fares.
The results include items dated after May 2024 (KFTC fines, 2025-2026 data). Since the deck is dated May 2024, I'll rely only on sources published before then. Next I'll check fares, the regulatory framework, and rival platforms.
Fares, EV taxi data, late-night shortages, and rival platforms are now covered. Next I'll check autonomous taxis, inbound tourism, licence values, driver income, and Kakao's business scale.
Several results I'd planned to use are dated after May 2024 (for example, the Seoul driverless taxi launch and the Dec 2024 KFTC fine), so I'll exclude them. Next I'll check demographics, autonomous-vehicle rules as they stood before May 2024, and LPG/EV taxi mix.
I have enough verified, pre-May-2024 evidence for the deck. Before building it, I'll check the sandbox's PDF tooling and fonts.
The sandbox has reportlab, matplotlib and DejaVu fonts. One fact I plan to use (Uber's March 2024 rebrand) so far appears only in a post-May source, so I'll look for a contemporaneous one.
I now have the verified facts for the deck. Before building it, I'll check glyph coverage in the fonts so symbols like ₩, → and ≈ render correctly.
Liberation Sans covers the symbols I need except ₩, so I'll use "KRW" in the text. Next I'll build the charts.
Charts are ready. Next I'll write the PDF builder with fixed slide geometry and an overflow check on every text block, so nothing gets clipped.
Now the slide content. I'm writing each cited point in my own phrasing with a source line on every slide.
The S6 gate block is about 5pt too tall for its allotted space. I'll widen that space slightly and re-run the build.
The PDF has 11 pages and no text runs off the page edges. Next I'll check for text collisions between blocks, such as a table overlapping the decision bar.
The overlap check found real layout problems: on slide 2 the opportunity heading sits on the growth-box, and on slide 3 the benchmark bullets run into the decision bar. I'll reflow those two slides, lift the decision bar slightly so the source notes clear it, and add an overflow check to the KPI tiles.
The "Policy fit" tile text is too long for its box. I'll shorten it and give the tiles a little more height.
No overlaps remain between text blocks. Next I'll check the vertical boundaries: that body text ends above the decision bar and that the source notes sit below it.
Layout is clean: body text ends above the decision bar and the source notes sit below it. Proofreading against the sources turned up several precision problems I need to fix:

- The income survey is from a 2021 publication, not 2020.
- The 3,000–4,000 car KPI doesn't match the stated 12–15% share.
- "Discretionary" licensing isn't what the source says.
- The 23% subsidy coverage is my own calculation, not the Seoul study's finding.

I'll correct these now.
All 11 replacements applied and the build still runs. I'll re-run the layout checks and then read the full extracted text for a final proofread.
The text flows correctly. One cosmetic fix: the numbered constraints on slide 2 also carry bullet dots, so I'll drop those. Next I'll read the remaining slides.
The remaining slides read correctly, and the appendix figures reconcile with the main slides. I'll make the final wording fixes (remove bullets from the numbered items, and tighten the slide 1 read-across sentence), rebuild, and run the checks again.
The layout is clean and the slide 2 numbered items now read as plain paragraphs. I'll copy the final PDF to the output folder and confirm it's there.
I've built the strategy deck as an 11-page landscape PDF: a cover, six core content slides, a discussion and decisions page, and three appendices (assumptions, source register, risk register).

**Deliverable:** `SuperK-Taxi_Korea_Deep_Dive_Strategy_May2024.pdf`

**Core recommendations**

- **Market reality:** Kakao's position is structural. Regulator data put its general-call share at roughly 
94% in 2021
. In franchise cabs its share rose 
to 73.7 percent in 2021, compared to 14.2 percent tallied in 2019
, and the regulator fined it for that favouritism. The deck therefore recommends a segment-first challenge rather than a head-on fight for general calls.
- **Supply is the binding constraint:** 
taxi calls more than tripled over two years while the number of taxi drivers decreased by over 8%
. Late-night calls are 
accepted only one in five times
. Plan A is an earnings floor, night-shift packages, corporate-fleet and lease partnerships, and driver scorecards.
- **Demand plan:** four segments with measurable service gaps: late-night commuters, airport and inbound visitors, corporate accounts, and a safety-first tier. Foreign riders' top complaint is entering addresses in a foreign language (44.5%).
- **Future-proofing:** take a franchise-licence decision by Q3 2024, prepare the platform-licence case for 2025, and treat autonomy as a partnership option. Government aims for 
at least one commercial Level 4 vehicle in 2027
. Electrification is gated by subsidies: 
electric taxis made up about 30% of the 111,583 newly registered taxis from 2021 to 2023
. On a Seoul case study's prices, the subsidy stack covers only about 23% of the price gap (my calculation).

**Caveats**

- **No internal data:** SuperK-T's own figures weren't supplied. Baselines are tagged [A] as working assumptions and must be validated by 30 June 2024. Targets are proposals.
- **Date discipline:** Only information public by May 2024 is used. Several search results were dated later (for example, the December 2024 fine and 2025–26 data), so I excluded them.
- **Illustrative numbers:** The earnings-floor cost (about KRW 1.8bn a year for 1,000 drivers) rests on stated assumptions. The exchange rate (about KRW 1,370 per US$) is assumed, and the EV price gap comes from one dated study.
- **Sources:** Seoul and national taxi-association data are used. I did not find a Korea Transportation Safety Authority report dated before May 2024 that was usable, so KOTSA appears only through a 2020 study on its driver-management data.