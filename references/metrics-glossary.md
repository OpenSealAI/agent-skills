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

Always state platform, market, language, keyword set, date range, and denominator. Cite evidence with `search_result_id` or `video_uid` (see `socialseal-data-contract.md`).
