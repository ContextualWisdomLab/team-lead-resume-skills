# Role Expansion Implementation Plan

> For agentic workers: use superpowers:executing-plans. Source research and fresh-context application checks may run independently.

**Goal:** 팀장급 이력서 스킬에 비기술 직무의 공식 채용 근거와 경력 증거 선택 기준을 추가하고 설치·공개 배포한다.

**Architecture:** 한 스킬의 공통 작성 절차와 직무별 참조표를 연결한다. 계산기와 외부 의존성은 늘리지 않는다.

**Tech Stack:** Markdown, YAML, 기존 Python 표준 라이브러리 계산기, Git.

**Spec:** `docs/superpowers/specs/2026-11-08-role-expansion-design.md`

## 검토 초점

공고 요구와 편집 판단, 인사권과 업무 리딩, 팀과 개인의 실적, 예상과 실현 값, 서로 다른 집계 범위를 구분한다. 합성 적용 결과를 일반 성능 향상으로 보고하지 않는다.

## Task 1: 기준 판본과 공식 출처

- [x] 공개 main과 개인 스킬 원격을 새로 확인하고 기준 판본을 보존한다.
- [x] 변경 전 스킬로 합성 영업·구매 과제 C를 실행하고 원문을 보존한다.
- [x] 추가 직무군의 공식 공고 본문을 직접 읽고 책임·자격·날짜·상태·한계를 기록한다.

## Task 2: 스킬 확장과 적용

- [x] 개인 스킬의 SKILL·evidence-workflow를 확장하고 role-families와 출처 장부를 작성한다.
- [x] 변경 후 과제 C와 경영지원 과제 D를 새 문맥에서 실행하고 기준별로 대조한다.
- [x] 실제 문제만 보완하고 최종 스킬 해시·출력·한계를 기록한다.

## Task 2B: 후속 MECE 요구

- [x] 10군 후보의 C/D 실제 읽은 파일과 출력·해시를 별도 보존한다.
- [x] 15개 기능의 포함·제외 경계와 산업·기술·관리 범위 태그를 정의한다.
- [x] ISCO·NCS 공식 근거와 맞춤 분류의 해석 한계를 기록한다.
- [x] 25개 합성 E 사례를 새 문맥에서 적용하고 단일 책임·복합 직무·미확정 처리를 대조한다.
- [x] 최종 분류를 별도 검토하고 실제 출력·해시·검증 한계를 기록한다.

## Task 3: 검증과 배포

- [x] 설치 단위 형식·참조 링크·기존 계산 테스트 9개를 확인한다.
- [x] 별도 검토자가 최종 스킬의 분류 경계·복합 책임·미확정 처리·출처 해석을 검토한다. 실제 적용 출력의 대조는 작성자가 수행하고 구분해 기록한다.
- [x] 개인 스킬을 일반 커밋·push하고 조정된 설치본을 확인한다.
- [ ] README·Architecture·Changelog·Gap·manifest를 갱신해 공개 저장소에 반영한다.
- [ ] 원격 main의 정확한 커밋·파일 트리를 대조하고 확장 범위와 한계를 전달한다.
