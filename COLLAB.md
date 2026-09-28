# Grok × ChatGPT collaboration

This repo is the shared lab notebook. Do not keep the real research only in a chat.

The two models cannot talk to each other. The owner pastes messages by hand.

## Relay rule

Every Grok or ChatGPT reply that needs the other model or the owner must end with one or both of these blocks. Copy the text inside the fence only.

### 1. GPT에 붙여넣기

Exact message for ChatGPT. No extra commentary inside the fence.

### 2. 직접 해줘야 하는 실험

Work only the owner can do: open a new GPT Project, time a run, paste raw output into an issue, click GitHub UI, use a paid model, etc.

Write the steps in order. Include the exact prompt, which URL or file to use, and where to paste the result.

If nothing needs to be relayed, omit both blocks.

## Roles

- **Human:** courier and experimenter. Pastes GPT↔Grok text. Runs tests the models cannot run.
- **Grok:** writes repo files, reviews incoming notes.
- **ChatGPT:** critique and parse runs. Does not rewrite the whole tree.

## Commit messages

Every commit title ends with `(grok)`, `(chatgpt)`, or `(human)`.

## How a turn works

1. Read `docs/hypothesis.md` and open issues first.
2. Put work in an issue comment, `research/log.md`, or `research/inbox/`.
3. Do not silently overwrite `docs/` or `src/`.
4. One claim per note.
5. Disagreement needs a falsifying test.

## Acceptance bar

- concrete claim
- what would falsify it
- what file it would change
- no 100M-memory platform, no production UI
