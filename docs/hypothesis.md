# Hypothesis

Structure conversation memory with multi-dimensional dynamic tags. Extract the same tags from a query, shrink the search space, then run semantic search. Goal: equal or better recall than vector RAG at a smaller active context.

Success:
1. Memory N grows, active context stays almost constant.
2. Tokens drop without losing recall.
3. Ambiguous time / project / state references beat vector RAG.
