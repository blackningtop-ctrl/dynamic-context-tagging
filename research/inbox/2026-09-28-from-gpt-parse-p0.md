# 2026-09-28 from-gpt parse P0

Source: issue #5 comment by owner.
Status: accepted as format test. Not accepted as latency data.

## Claim

A short DCT parse harness can keep ChatGPT on one-pass structured tags for the 5 stock queries, with zero invented project names.

## Falsify

A clean Custom GPT/Project run (harness body only + `속도 테스트`) breaks format, invents a project, or splits extraction.

## File change if accepted later

Keep harness short. Add modifier-scope rule for temporal+deprecated.
