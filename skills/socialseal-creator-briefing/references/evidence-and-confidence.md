# Evidence and Confidence

SocialSeal evidence is not all the same kind of thing. Mixing the kinds is the most common analysis error: it produces both overconfidence ("this hook will work") and underconfidence ("the data is noisy, ignore it"). Use these three tiers and state which one a claim rests on.

## Tier 1: Hard measurements (exact observations, not estimates)

These are direct observations of the social-search surface at the time SocialSeal captured it:

- search results and their rank/position for a tracked query
- presence or absence of a brand, competitor, creator, or content pattern in those results
- discoverability and keyword coverage (where an entity appears across the tracked keyword set)
- share of voice within a stated scope
- the latest engagement snapshot (views, likes, comments, shares, saves) for a surfaced video

There is no approximation or sampling error in these numbers. They are what SocialSeal saw. If results vary day to day, that is because the underlying social-search reality changed (the platform re-ranked, new videos surfaced, old ones dropped), **not** because the measurement is imprecise.

Implication: do not hedge a hard measurement as if it were a noisy estimate. "Owned content appeared for 3 of 20 tracked keywords on `<date>`" is a fact, not an approximation. Report movement plainly and attribute it to a changing search reality, with the capture dates.

## Tier 2: Statistics on this data carry selection bias

Every metric above is computed over a biased sample by construction: SocialSeal only sees **high-ranking videos for the queries you chose to track**. It does not see the whole platform, the whole category, or videos that never surface for those queries.

So any statistic describes "what surfaces for these tracked queries in this scope," not total market demand, total category supply, or what every user sees. State this scope explicitly and never extrapolate past it.

Safe phrasing:
- "Among videos that surface for these 20 US TikTok keywords, creators hold ~70% of surfaced attention." (correct: scoped)
- "70% of TikTok travel content is made by creators." (wrong: extrapolates to the whole platform)

Practical rules:
- always state the denominator and the scope (platform, market, language, keyword set, date range)
- do not infer total demand, total supply, or audience size from surfaced results
- a keyword with zero surfaced owned content is a presence gap, not proof of audience demand or its absence
- if the keyword set changed between periods, comparisons are directional only; say so

## Tier 3: Creative exemplars are anecdotal, not proof

When you analyze reference videos to derive a hook, hero shot, structure, or concept, you are reasoning from examples that already surfaced. That is a strong starting point, but it is **anecdotal evidence for creative direction**, not proof that a given hook or concept will perform for the user.

Exemplars tell you "this surfaced for this query," not "this caused the result" and not "this will work for you." Survivorship is baked in: you see what surfaced, not the many similar videos that did not.

Safe phrasing:
- "Multiple surfacing exemplars open on a first-person cost reveal; worth testing as a hook." (correct: pattern + test framing)
- "A first-person cost reveal is proven to win, so do that." (wrong: treats anecdote as proof)

Practical rules:
- a pattern needs multiple exemplars or an explicit reason a single example matters; one video is an anecdote
- frame creative recommendations as hypotheses to test and measure, not guarantees
- the blueprint engine compiles best practices from exemplar evidence; that raises confidence but does not convert anecdote into proof
- avoid the words "proof", "proven", "guaranteed", or "will work" for creative bets; use "evidence suggests", "worth testing", "consistent with"

## One-line confidence labels

Attach a confidence basis to recommendations:

- **Measured:** rests on a Tier 1 hard observation (cite the figure, scope, and capture date).
- **Scoped statistic:** a Tier 1 figure aggregated; state the denominator and selection-bias caveat.
- **Indicative pattern:** a Tier 3 creative read from multiple exemplars; frame as a test.
- **Single-example / metadata-only:** weakest; one exemplar, or titles/captions without viewed analysis.
