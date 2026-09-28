# Manual holdout

Do not generate these queries with GPT or Grok and call them human.
Need 50–100 lines in `manual_holdout.jsonl`.

Each line:
```json
{"id":"q001","query":"...","gold_ids":["mem_..."],"notes":""}
```

Rules:
- query is something the owner would actually type to recall a project
- gold_ids point at real or accepted memories
- no `d-043` style synthetic ids unless the owner mapped them on purpose
