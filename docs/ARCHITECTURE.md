# Portfolio 구조와 파이프라인

## 책임
Portfolio는 공개 후보 프로젝트 evidence의 원본과 사람용 설명을 보유한다.
Agent는 이를 읽어 private 공고·프로필과 비교한다. 원본 프로젝트 코드를 실행하는 곳도,
사용자 사실·지원 기록을 수집하는 저장소도 아니다.

```text
원본 프로젝트의 고정 revision + 검토한 근거
    → data/public/portfolio.json  (공개 메타데이터 원본)
    → scripts/check_portfolio.py (계약·해시·사례 구조·링크 검사)
    → generated/PROJECT_INDEX.md (유일한 자동 생성 Markdown)
    → README.md / projects/*.md  (사람이 관리하는 서술; 자동 덮어쓰기 금지)

Career Agent src/career_agent/public_contract.py (canonical 계약)
    → scripts/public_contract.py (바이트 동일 복제)
    → contracts.lock.json + schemas/career-public-v1.schema.json

공개 portfolio.json → Career Agent validate / prepare → Agent private 미검토 메모
Agent private 프로필·지원서·DB → Portfolio 역방향 전송 없음
```

위 화살표는 데이터 의존성과 작업 순서다. README/사례를 프로그램이 자동 생성한다는 뜻이 아니다.
실제 명령·갱신 순서는 [DEVELOPMENT](DEVELOPMENT.md)를 따른다.

## 변경에 따른 검증 범위
문서 구조만 바꿀 때는 원본 성과·공개 JSON·contract lock을 바꾸지 않는다.
성과 snapshot 갱신은 원본 revision을 새로 읽고 JSON·사례·생성 인덱스를 함께 검토한다.
공개 계약 변경은 Agent canonical → Portfolio 복제본/lock/Schema → 양쪽 회귀 순서다.
Agent의 private 회사분류 모델을 바꾸는 것만으로 공개 계약을 개정하지 않는다.

## 해석 경계
ownership은 책임 확인이고 evidence는 연결된 근거이며 proficiency/eligibility는 별도 판단이다.
고정 snapshot은 원본 프로젝트의 실시간 상태가 아니다. 뒤의 원본 작업이 완료됐더라도
해당 근거를 읽고 이 저장소를 갱신하기 전에는 기존 snapshot의 한계를 보존한다.
새 구조와 장기 규칙은 이 문서, 현재 우선순위는 [STATUS](STATUS.md), 세부 계약은 [DATA_MODEL](DATA_MODEL.md)에 둔다.
