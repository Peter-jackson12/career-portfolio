# 문서 지도

새 작업의 읽기 순서: 원격 main/PR/CI 확인 → [AGENTS](../AGENTS.md) → [STATUS](STATUS.md) → 필요한 문서만.
현재 PR의 변경을 검토한다면 main과 섞지 말고 그 PR HEAD의 문서를 읽는다.

| 알고 싶은 것 | 기준 문서 | 여기에 중복하지 않을 것 |
|---|---|---|
| 현재 snapshot, 다음 작업, 미확인 상태 | [STATUS](STATUS.md) | 실시간 PR/CI를 확정하는 주장 |
| 저장소 구조·생성 순서·Agent 연결 | [ARCHITECTURE](ARCHITECTURE.md) | 개인 경력과 지원 기록 |
| 공개 데이터와 계약 | [DATA_MODEL](DATA_MODEL.md) | Agent의 private enrichment 모델 |
| 설치·검증·계약 동기화 명령 | [DEVELOPMENT](DEVELOPMENT.md) | 매일의 테스트 수 복제 |
| 공개 전 개인정보 확인 | [PRIVACY](PRIVACY.md) | 실제 개인정보 값 |
| 프로젝트 책임 확인의 의미 | [OWNERSHIP](OWNERSHIP.md) | 기술 숙련도/자격 인증 |
| 프로젝트별 서술과 근거 | [Stock](../projects/stock.md), [Airplane](../projects/airplane.md), [근거 인덱스](../generated/PROJECT_INDEX.md) | 원본 저장소 전체 복제 |
| 이후 방향·과거 검토 | [ROADMAP](ROADMAP.md), [감사 기록](AUDIT_20260922.md) | 완료되지 않은 기능을 완료로 표시 |

## 두 저장소의 문서 책임
[Career Agent](https://github.com/Peter-jackson12/career-agent)가 전체 취업 파이프라인, 회사 facts/선호 정책,
원격·로컬 운영 절차와 짧은 인계 템플릿을 소유한다. 해당 저장소의 AGENTS.md와 docs/INDEX.md에서 시작한다.
Portfolio에는 공개 근거와 계약 소비/생성 경계만 둔다. Agent private 자료를 역방향으로 받지 않는다.
두 저장소 PR이 아직 병합되지 않았다면 그 PR HEAD에서 신규 문서를 읽는다.
