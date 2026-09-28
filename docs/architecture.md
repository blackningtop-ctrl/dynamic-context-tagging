# Architecture

Write: conversation -> one-pass decomposer -> tags + event memory -> SQLite + vector index.
Read: query -> query tags + temporal range -> tag filter (0 LLM tokens) -> semantic search -> optional CE -> top-K active context.

Active-context size stays flat only if the query hits a **bounded partition** (project/namespace/bucket whose matching set does not grow with global N). Topic labels alone do not bound the set.
