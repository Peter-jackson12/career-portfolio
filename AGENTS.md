# AGENTS.md

## 목적과 읽기 순서
사람이 읽는 공개용 커리어 인터페이스다. 한국어로 작업한다.
README → docs/ROADMAP → docs/DATA_MODEL → 수정할 프로젝트의 원본 근거를 읽는다.
원본 프로젝트 구현·실험 결과는 원본 저장소가 담당하며 여기에는 요약과 고정 출처를 둔다.

## 원칙
수치·성과·상태를 바꾸기 전에 원본 README·코드·테스트·실행 근거를 확인한다.
성능 향상·배포·실데이터 검증·운영 성과와 개인 단독 기여를 추측하지 않는다.
실패와 한계를 보존하고 첫 화면은 짧게 유지한다. 상세는 사례와 원본으로 연결한다.
연락처·실명·주소·이력서 원문·지원 이력·key·token을 추가하거나 접근 공개 범위를 자동으로 넓히지 않는다.

## 데이터와 생성
public JSON은 이 저장소가 소유하고 실행 계약은 Career Agent의 canonical을 그대로 복제한다.
계약 변경은 양쪽 회귀·contracts.lock.json·Schema를 함께 검토한다.
자동 생성 대상은 generated/PROJECT_INDEX.md뿐이다. README·사례의 사람 편집 narrative를 덮어쓰지 않는다.
Agent private 데이터는 역방향 전송하지 않는다. 기술 태그는 개인 숙련도나 human verification이 아니다.
사례는 docs/PROJECT_CASE_STUDY_TEMPLATE.md의 My Role·설계 결정·결과·한계까지 포함한다.

## 검증과 Git
python scripts/check_portfolio.py --tracked, python -m pytest -q를 실행한다.
가능하면 --agent-root로 두 계약의 바이트 일치도 확인한다. 생성 인덱스는 --write로 갱신한다.
브랜치 → 의미 있는 커밋 → PR → self-review/CI → 최신 head 확인 순서를 지킨다.
실행하지 않은 검증을 통과했다고 쓰지 않는다. 공개 전에는 docs/PRIVACY.md의 이력·metadata 점검이 필요하다.
