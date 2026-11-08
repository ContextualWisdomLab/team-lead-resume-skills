# Team Lead Resume Implementation Plan

> For agentic workers: use `superpowers:executing-plans` for implementation. Research and independent application checks may run in separate contexts.

**Goal:** 출처가 있는 팀장급 이력서 작성 스킬을 만들고 설치·검증·커밋한다.

**Architecture:** 스킬은 문서 중심이며 경력 기간 계산만 작은 로컬 스크립트로 제공한다. 기존 한국어 스킬과 문서 형식 스킬은 각자의 책임 범위를 유지한다.

**Tech Stack:** Markdown, YAML, Python 3.10+ 표준 라이브러리, Git.

**Spec:** `docs/superpowers/specs/2026-11-08-team-lead-resume.md`

## 제약과 검토 초점

- 공개 채용 요구와 실제 합격 사례를 혼동하지 않는다.
- 합성 평가만 사용하며 개인 자료를 저장하지 않는다.
- 겹친 기간과 불명확한 경력 인정, 인사권 없는 리딩, 정성 효과, 타인 구현, 지정 양식의 입력을 점검한다.
- 계산은 시작·종료 월을 포함하는 참고값이며 정확한 일수나 채용사 경력 인정 결과가 아니다.
- 스킬 작성·검증·설치는 개인 스킬 체크아웃에서 수행하고, 완성본만 새 저장소에 옮긴다.

## Task 1: 출처 조사와 스킬 작성

- [x] 기존 한국어 이력서 지침과 사용 범위를 읽는다.
- [x] 스킬 없는 합성 과제의 응답을 확보한다. 이미 맞은 행동을 실패로 꾸미지 않는다.
- [x] 공식 채용 공고와 채용 지침을 직접 열어 출처·날짜·상태·적용 한계를 기록한다.
- [x] `SKILL.md`와 3개 근거 파일에 입력→JD 대응→사실 대조→작성→검증 절차를 쓴다.
- [x] 별도 문맥에서 같은 합성 과제와 다른 직무 조건의 과제를 수행하고 원문 결과를 보존한다.

## Task 2: 재직 기간 계산

**Interface:** `python3 scripts/career_months.py INPUT.json --as-of YYYY-MM`는 `start`, `end`(현재는 null), `include`(boolean) 기록의 월 합집합을 JSON으로 출력한다. 제외 기록에는 `reason`이 필요하다.

- [x] `tests/test_career_months.py`를 먼저 쓴다. 66개월과 62개월의 10개월 중복은 118개월, 9년 10개월이어야 한다.
- [x] 스크립트 미구현으로 테스트가 실패함을 확인한다.
- [x] 스킬 경로에 계산기를 작성한다. 명시하지 않은 포함 여부, 역전 기간, 미래 종료일, 잘못된 월은 오류로 처리한다.
- [x] 전체 테스트와 실제 CLI 호출을 실행한다.

## Task 3: 저장과 확인

- [x] 설치 경로의 스킬 형식 검사와 독립 합성 과제 검토를 끝낸다.
- [x] 연구·검증 범위와 남은 Gap을 README·문서에 기록한다.
- [x] 개인 스킬을 저장하고 원격 경로를 다시 확인한다.
- [x] 완성본을 새 로컬 Git 저장소에 커밋한다.
- [x] 사용자의 후속 지시에 따라 GitHub 공개 저장소를 만들고 올린 뒤 원격 SHA를 확인한다.
- [x] 설치·로컬 커밋·원격 저장소 상태를 구별해 결과를 정리한다.
