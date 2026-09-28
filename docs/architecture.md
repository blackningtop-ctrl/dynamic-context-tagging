# Architecture

Write: conversation -> one-pass decomposer -> tags + event memory -> SQLite + vector index.
Read: query -> query tags + temporal range -> tag filter (0 LLM tokens) -> semantic search -> rerank -> top-K active context.
