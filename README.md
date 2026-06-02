# divelog

실리콘밸리 풀스택 개발자를 목표로 하는 학습 기록 레포.
멘토 에이전트(Claude Code + CLAUDE.md)가 매 세션을 진행하고 `progress.md`에 기록한다.

---

## 현재 진행 상황

**시즌 1** — 멘토 에이전트 풀스택 대시보드

| 항목 | 내용 |
|---|---|
| 메인 트랙 | FastAPI + React |
| 목표 | 오답노트 조회/관리·세션 로그 시각화 웹 대시보드 |
| 현재 단계 | FastAPI 세팅 + `/health` 엔드포인트 완료 |
| 다음 단계 | `GET /progress` — progress.md 파싱 후 JSON 반환 |

---

## 학습 기록

- 상세 진행 상황·오답노트·세션 로그 → [`progress.md`](./progress.md)

---

## 로컬 실행

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

`http://localhost:8000/docs` — Swagger UI
