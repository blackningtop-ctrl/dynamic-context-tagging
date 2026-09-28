# Architecture

Write: conversation -> one-pass decomposer -> tags + event -> SQLite + vector index.
Read: query tags -> bounded partition filter -> semantic search -> optional CE -> top-K.

Active context stays flat iff the matching partition does not grow with N.
If a project bucket overflows, split+parent-fallback preserves recall but the parent set grows with the project. Single-leaf routing keeps the set small and drops gold on wrong shards.
