# Dynamic Context Tagging (DCT)

장기 기억을 크게 유지하면서도, 질문마다 LLM이 읽는 Active Context는 작고 정확하게 유지하기 위한 메모리/컨텍스트 아키텍처 연구.

> **목표:** Memory 총량 N이 증가해도 질의당 삽입 Memory Token은 거의 일정하게 유지한다.

Grok×ChatGPT가 이 레포에서 같이 연구한다. 협업 규칙은 [COLLAB.md](COLLAB.md).

## 한 줄 정의

대화와 장기 기억을 시간·주제·프로젝트·상태·관계 등의 동적 태그로 구조화하고, 질문에서도 같은 의미 태그를 추출해 필요한 기억만 선택적으로 활성화한다.

## 가설

다차원 Dynamic Tag로 검색 공간을 먼저 줄인 뒤 Semantic Search를 적용하면, Vector RAG보다 적거나 비슷한 Active Context Token으로 동일하거나 높은 Memory Recall을 얻을 수 있다.

## 레포 구조

- `docs/` 합의된 설계
- `src/dct/` 프로토타입
- `data/examples/` 골든 메모리/질의
- `experiments/` 실험 계획과 결과
- `research/` 로그와 GPT/Grok inbox

## 빠른 시작

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m dct.demo
```

MIT License
