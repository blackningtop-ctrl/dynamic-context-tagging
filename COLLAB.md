# Grok × ChatGPT collaboration

This repo is the shared lab notebook. Do not keep the real research only in a chat.

## Roles

- **Human:** decides what to keep, pastes the other model's output into an issue or PR when needed.
- **Grok:** repo owner side. Writes files, runs code, opens issues, reviews incoming notes.
- **ChatGPT:** review / critique / alternative design. Prefer comments on issues and proposed doc diffs over rewriting the whole tree.

## How a turn works

1. Read `docs/hypothesis.md` and the open issues before proposing anything new.
2. Put work in one of:
   - issue comment (review, disagreement, question)
   - `research/log.md` (dated note)
   - a small file under `research/inbox/` named `YYYY-MM-DD-short-slug.md`
3. Do not silently overwrite `docs/` or `src/` with a full rewrite. Propose a patch.
4. One claim per note: hypothesis change, experiment result, or design objection.
5. If you disagree, write the objection and the test that would settle it.

## What belongs where

| Place | Use |
|---|---|
| `docs/` | Agreed design. Change only after a note is accepted. |
| `src/` | Running prototype. |
| `data/examples/` | Gold memories and queries. |
| `experiments/` | Planned runs and measured results. |
| `research/log.md` | Chronological decisions. |
| `research/inbox/` | Fresh GPT/Grok notes waiting for merge. |
| Issues | Tasks and reviews. |

## Issue labels

- `research` — design / writing
- `experiment` — something to measure
- `poc` — code
- `from-gpt` — arrived from ChatGPT
- `from-grok` — arrived from Grok
- `needs-human` — only the owner can decide

## Acceptance bar

A note is ready to merge into `docs/` when it has:

- a concrete claim
- what would falsify it
- what file it would change
- no new product scope (no 100M-memory platform, no production UI)
