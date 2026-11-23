# Storage/query-processing depth review

Date: 2026-11-05. This finishes one bounded continuation of the independent source-aware audit. It does not certify the 945 source-section inventory entries or the whole course.

Read all 22 lesson bodies: AD23–AD37 and AD74–AD80. Modified 20 in this continuation; AD23 and AD28 retained their prior fixes. Read the proposal mappings without changing them. Source review used the exact selected raw-text windows below, rather than claiming every mapped section was fully re-audited.

## Concrete findings and repairs

| Finding | Lesson | Source | Repair |
|---|---|---|---|
| SD01 | AD24 | 13.3.1 | Added max-map algorithm, eight-page trace, recheck/quantization boundary, termination/proof, independent exercise 5 and worked answer. |
| SD02 | AD26 | 13.7 | Added divmod address calculation, append example, bounds/publication condition, and exercise/answer 5. |
| SD03 | AD29 | 24.5.2.2, 24.5.2.3 | Added buddy guards, full alias redirection, shrink loop, exact trace/proof and exercise/answer 5. Labeled coalesce as a PE solution to source exercise and linear hashing as extension to the source bibliographic mention. |
| SD04 | AD35 | 16.2.1, 16.2.4, 16.3.5 | Added guarded bag-preserving filter proof, join/projection/group/outer-join examples, fixed-point worklist with finite-space/closure proof, distinct propagation bounds and empty-result boundary; independent exercises/answers 5–6. |
| SD05 | AD36 | 16.4.1 | Added explicit singleton-index inner branch to both base and physical-property recurrences; inner residual filters retained and inner scan excluded. Existing property-aware proof and counterexample retained. |
| SD06 | AD37 | 16.5.2.3, 16.6.1, 16.6.3 | Added row_count/nonnull_count/sum invariant, signed insert/delete rules, zero/all-NULL/empty trace, grouped-versus-scalar boundary, exercise/answer 5; manually repaired prose. |
| SD07 | AD75 | 24.1 | Added six actual bit/query states using positions 0..7, prepared-model label and independent-transfer boundary; repaired MAYBE/FOUND, m/k/hash notation and prose. |
| SD08 | AD77 | 15.5.1, 15.5.2, 15.5.3 | Added six actual nested-loop cursor/check/emit states for four matches and six checks, prepared-model/cost label; repaired prose and pseudocode predicate. |
| SD09 | AD78 | 16.4.4 | Manually restored words and expression labels, preserved existing semijoin proof, NULL counterexample and scalar-count repair. |
| SD10 | AD79 | 20.6 | Pointed 2PC to authored AD50; repaired IaaS and capacity prose spacing. |
| SD11 | AD80 | 22.5.3, 22.7.5 | Added E1/E2 join-key repartition, E3 group-key repartition, partial/final aggregation and blocking boundary; signed insert/delete/group-key-update routes with local materialized input/output invariant; exercise/answer 5. |
| SD12 | Scoped 22 | Readability only | 340 explicitly curated replacement occurrences across 19 lessons in the initial pass, followed by contextual correction and numbered-list spacing repairs. Fenced code was excluded from bulk replacements; pseudocode wording fixes were made explicitly. |

## Per-lesson conclusion

| Lesson | Scope/result |
|---|---|
| AD23 | Confirmed existing XOR parity proof/update formula, elevator batch trace, stable-storage/failure assumptions and numeric answers; no content change in this continuation. |
| AD24 | Fixed hierarchical map depth; retained slot/RID/generation, compaction and allocation invariants. |
| AD25 | Confirmed existing loading/resident/error state and force/pin distinction; repaired prose. |
| AD26 | Fixed chunk addressing; retained position/null/version preservation proof. |
| AD27 | Confirmed existing search/insert/internal split/occupancy and utilization examples; repaired prose/pseudocode words. |
| AD28 | Confirmed prior internal pointer/separator repair and root contraction; no content change in this continuation. |
| AD29 | Fixed merge/shrink and source attribution; retained low-bit split and linear routing proofs. |
| AD30 | Confirmed existing bitmap validity/RID crossover and current/history temporal examples; repaired prose. |
| AD31 | Confirmed prior stepped/basic cost, rolling progress, tombstone/snapshot retention and buffer-tree coverage; repaired notation. |
| AD32 | Confirmed prior multi-page merge buffers, seeks/pass boundaries and empty/fit cases; repaired prose. |
| AD33 | Confirmed prior multiplicity/partition proof, hybrid cost and heavy-key fallback; repaired prose. |
| AD34 | Confirmed iterator cleanup, bag/set counts, partial AVG and blocking boundaries; repaired prose. |
| AD35 | Fixed guarded rewrite/worklist and distinct-propagation depth. |
| AD36 | Confirmed property-state recurrence/proof; corrected indexed-inner scan accounting in actual recurrences. |
| AD37 | Fixed grouped delta state and repaired top-K/Halloween/adaptive prose. |
| AD74 | Confirmed duplicate-spanning-block counterexample, lookup cost and index update boundaries; repaired prose. |
| AD75 | Added concrete Bloom states and repaired notation; retained existing probability assumptions/derivation. |
| AD76 | Confirmed candidate completeness for AND/OR and residual filtering; repaired prose. |
| AD77 | Added concrete nested-loop states and repaired readable cost/algorithm wording. |
| AD78 | Confirmed semijoin multiplicity proof, NULL anti-join trap and scalar COUNT restoration; repaired prose. |
| AD79 | Confirmed source locations for distributed/cloud service content; corrected AD50 cross-reference. |
| AD80 | Fixed multi-exchange composition and signed maintenance routing, retained task/attempt commit and scheduling model. |

## Exact source excerpt scope

Line numbers are 1-based in the local extracted `.txt` files. These selected displayed windows were read for the cited mechanism; they are not claims that every source page or figure in each section was inspected. Full paths and source hashes are in the JSON report.

| Source text | Selected raw-text lines | Focus |
|---|---|---|
| chapter-12.txt | 518–573, 799–863 | RAID parity/update equation and levels; elevator scheduling, extents, nonvolatile write buffer |
| chapter-13.txt | 296–374, 444–500, 914–1021, 1119–1168, 1169–1223, 1397–1453 | Variable records/slotted pages; hierarchical max free-space map; pin/shared-exclusive/output/force; write reordering; column layout and chunked main-memory arrays |
| chapter-14.txt | 138–166, 338–356, 409–478, 901–949, 1055–1150, 1311–1396, 1715–1756, 1811–1825, 1991–2036, 2328–2375 | Dense/sparse/multilevel/update; B+ insertion/deletion/redistribution/relocation/strings; multiple-key and covering; buffer trees; current/history temporal index |
| chapter-15.txt | 588–686, 700–719, 755–796, 816–853, 1134–1170, 1185–1227, 1248–1255, 1363–1407, 1486–1521, 1608–1635 | External-sort transfer/seek formulas; tuple/block/index loops; hash recursive/overflow/cost; hybrid setup; projection/set/aggregation; demand/producer-driven pipeline |
| chapter-16.txt | 182–397, 561–622, 644–685, 725–763, 845–981, 1003–1126, 1322–1431, 1538–1564, 1591–1645, 1699–1761, 1786–1826 | Equivalence guards/worklist enumeration; catalog/histogram/selection/join/distinct estimates; DP/indexed-loop exception; semijoin; aggregate maintenance; top-K/Halloween/parametric/adaptive |
| chapter-20.txt | 1054–1098, 1158–1201, 1235–1261, 1396–1438 | Distributed/local/global boundaries; 2PC overview; cloud service models/elasticity and benefits/limitations |
| chapter-22.txt | 703–744, 811–920, 920–967, 1125–1159, 1208–1257, 1303–1379 | Exchange model; join→group plan and partial aggregation; task replay; parallel plan properties; optimization heuristics; parallel view-maintenance routing |
| chapter-24.txt | 13–40, 68–144, 182–281, 466–489, 1028–1038, 1137–1269 | Bloom build/test; basic/rolling/stepped merge and amortized cost; bitmap/RID crossover; extendible deletion/coalescing exercise, overflow and linear-hashing bibliographic boundary |

## Verification and limits

42 independently recomputed model/example checks passed, including a 12-expression three-relation worklist closure, nine NULL-flag filter-pushdown fixtures, Bloom bitsets, join multiplicities, buffer/cost arithmetic, and full recomputation of the AD80 insert/group-update result. All 22 structural checks passed: required sections, balanced fences, matching exercise/answer numbering and no replacement characters. The AD75 and AD77 prepared stateboards each contain six concrete states. Detailed actual/expected values are in the JSON.

The initial manual spacing pass made 340 curated replacements across 19 lessons; contextual fixes and list-spacing corrections followed. Bulk replacement excluded code fences; pseudocode wording fixes were explicit.

No native SQL or web runner was executed, and no new engine/runtime measurement is claimed. Adjacent §17.3, §18.11 and §3.8 references were not independently reread in this pass. Prepared model traces and finite checks do not certify production implementations or every learner input. Proposal titles/allocations remain unchanged, including the older AD79 proposal title.

All concrete findings raised during this bounded pass are repaired. Broader source completeness, rendered-course QA and whole-bank semantic review remain outside this report.
