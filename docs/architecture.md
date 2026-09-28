# Architecture

Read path: query tags -> bounded partition -> vector -> optional CE.

Hot/archive: keep a recency cap in the hot set. Escalate on licensed old-time queries or empty hot.
If a fixed share of queries escalate into a growing archive, mean candidates track that archive. A bounded summary peek stays small and drops gold. Same tradeoff as split+fallback.
