# Metrics Glossary

- **Discoverability:** how often a brand, competitor, creator type, or content pattern appears across the selected keyword set and platform scope.
- **Keyword coverage:** share of tracked keywords where the entity or pattern appears.
- **Share of voice:** qualified surfaced attention for an entity divided by total qualified surfaced attention in the same scope.
- **Owned content:** content published by the brand's own account(s).
- **Creator content:** content published by creators, partners, media, affiliates, or customers.
- **Qualified result:** a surfaced result that matches the search intent and analysis scope.

## Deriving surfaced attention

"Surfaced attention" for share of voice is derived from real export fields, not invented:

- weight qualified results by `rank`/position (higher rank = more surfaced attention) and/or by the latest `views_count` snapshot.
- always compute against a stated denominator (total qualified surfaced attention in the same scope).
- when metrics or rank are missing, fall back to keyword coverage and say so; do not present a share-of-voice number you cannot ground.

Always state platform, market, language, keyword set, date range, and denominator. Cite evidence with human-readable references (the `"keyword" [market, platform]`, the video title/URL, and `@author_handle`), keeping `video_uid`/`search_result_id` only as an internal traceability note (see `socialseal-data-contract.md`).

## What these numbers are (and are not)

These metrics are hard observations of the social-search surface, not estimates: see `evidence-and-confidence.md`. Day-to-day variation reflects a changing search reality, not measurement error. But every figure is computed over a biased sample (only high-ranking videos for the tracked queries), so it describes "what surfaces for these queries in this scope," never total market demand or whole-platform supply.
