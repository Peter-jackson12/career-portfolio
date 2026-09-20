# Portfolio Roadmap

## 방향
이 저장소는 **템플릿 자체를 보여주는 프로젝트가 아니라, 실제 프로젝트를 빠르게 이해시키는 인터페이스**로 만든다.

레퍼런스에서 가져올 요소:
- GitHub `gitfolio`: Hero / About / Projects / Contact처럼 단순한 정보 구조와 GitHub Pages 자동 배포 방식
- `techfolio`: 주요 프로젝트를 별도 case study 페이지로 깊게 들어가는 구조
- 데이터 포트폴리오 사례들: 프로젝트명 · 설명 · 기술 · 증명하는 역량을 한 화면에서 비교하는 표

통째로 포크하지 않는 이유:
- 포트폴리오의 핵심은 템플릿 코드보다 Stock/Airplane 등 실제 작업의 설명이다.
- fork 관계와 원본 템플릿의 구조를 그대로 끌고 오면 불필요한 파일과 디자인 결정까지 상속된다.
- 필요한 UI만 나중에 독립적으로 구현하면 저장소의 목적과 커밋 이력이 더 명확하다.

## Phase 1 — Content Foundation
- [x] 포트폴리오 허브 README
- [x] 프로젝트 case study 공통 규격
- [x] 에이전트 작업 원칙
- [ ] Stock case study
- [ ] Airplane case study
- [ ] KRX Quant EDA case study
- [ ] 통계/실험계획 프로젝트 요약
- [ ] 자기소개 / 목표 직무 / 연락처 공개 범위 확정

## Phase 2 — Web Portfolio
- [ ] 콘텐츠와 UI 분리 구조 설계
- [ ] 반응형 홈: Intro / Featured Projects / Skills / Learning / Contact
- [ ] 프로젝트별 상세 페이지
- [ ] GitHub Pages 또는 다른 정적 호스팅에 자동 배포
- [ ] 모바일/접근성/링크 검증

## Phase 3 — Resume Integration
- [ ] 웹 포트폴리오의 핵심 문장을 1~2페이지 이력서용으로 압축
- [ ] 프로젝트별 이력서 bullet과 case study의 근거 연결
- [ ] PDF/웹/GitHub의 프로젝트 명칭과 수치 일치 검증

## 공개 전 체크
- 개인정보/연락처 공개 범위
- 프로젝트별 최신 상태와 수치
- 깨진 링크
- 이미지 및 외부 템플릿/자산의 라이선스
- 비공개 데이터나 로컬 경로 노출 여부