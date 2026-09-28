# 가설과 성공 조건

## Hypothesis

대화 및 Memory를 다차원 Dynamic Tag로 구조화하고, Query에서도 동일한 방식으로 Tag를 추출해 검색 공간을 먼저 줄인 뒤 Semantic Search를 적용하면, 기존 Vector RAG보다 적은 Active Context Token으로 동일하거나 높은 Memory Recall을 얻을 수 있다.

## 성공 조건

1. Memory 총량 증가 → Active Context는 거의 일정
2. Token 감소 → Retrieval Recall 유지 또는 증가
3. 모호한 시간/프로젝트/상태 참조 → Vector RAG보다 정확
