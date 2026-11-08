# Team Lead Resume Skills

공식 채용 공고와 실제 경력 증거를 연결해 **팀장급 이력서·경력기술서·자기소개서**를 작성하고 검토하는 Agent Skill입니다. 첫 판은 한국어 IT·개발·데이터·AX 리더 직무를 중심으로 조사했습니다.

스킬 이름은 **`team-lead-resume`**입니다. 사람 관리, 기술 판단, 프로젝트 실행, 사업 성과를 실제 책임에 맞춰 보여 주도록 돕습니다.

## 제공 기능

- 채용 공고의 필수·우대·업무 요구와 실제 경험을 연결하는 JD 대응표
- 공식 직책, 직속 인원, 프로젝트 인원, 채용·평가·예산 권한의 구분
- 기획·구현·검수, 개인 행동·팀 결과, 납품·현업 사용·사업 효과의 구분
- 기준값·비교값·기간·분모·산식이 확인되는 성과 서술
- 겸직·겹친 기간을 중복 제외하는 월 단위 경력 계산기
- 지원자의 경력 흐름과 관점을 보존하는 한국어 요약·경력기술서 작성
- 회사 지정 양식·문항 순서 우선, DOCX/PDF 렌더·텍스트 추출 검증 지침
- 제출 문서와 내부 근거표·확인 질문의 분리

정기 면담의 개최만으로 코칭 내용이나 육성 효과를 만들지 않습니다. 실제 인사관리 권한과 성과가 확인되면 구체적으로 제시합니다.

## 사용 예

```text
$team-lead-resume
첨부한 채용 공고와 경력 자료를 대조해 팀장급 이력서와 경력기술서를 작성해 주세요.
회사의 지정 양식과 문항 순서를 유지하고, 개인 역할과 팀 결과를 구분하세요.
미확인 수치·직함·인원·경력 인정 여부는 추정하지 말고 별도 확인 사항으로 알려 주세요.
```

입력으로 공고 원문/URL, 경력 자료, 제출 양식, 원하는 문서 종류와 형식을 제공합니다. 자료가 부족한 항목은 확인하고 나머지 작성을 진행합니다. 실제 지원서 제출과 채용담당자 전송은 별도의 사용자 요청이 필요합니다.

## 구성

| 경로 | 내용 |
| --- | --- |
| [SKILL.md](skills/team-lead-resume/SKILL.md) | 스킬의 시작점과 작성·검토 절차 |
| [채용 사례와 출처](skills/team-lead-resume/references/hiring-cases.md) | 공식 공고·역할·이력서·ATS 지침, 날짜와 적용 한계 |
| [경력 증거 절차](skills/team-lead-resume/references/evidence-workflow.md) | 책임·성과·연수 검산·AX 경험·합성 예문 |
| [작성과 제출](skills/team-lead-resume/references/writing-and-delivery.md) | 한국어, 지정 양식, 분량, 파일 검증 |
| [월 계산기](skills/team-lead-resume/scripts/career_months.py) | 포함을 명시한 기간의 합집합 계산 |
| [평가 기준](evaluations/criteria.md) | 합성 입력의 판정 기준과 한계 |
| [검증 기록](evaluations/review.md) | 실제 출력·수정·확인 결과 |

`skills/team-lead-resume/` 전체가 설치 단위입니다. 에이전트 환경의 정식 스킬 설치 절차에 이 폴더를 사용하세요. `SKILL.md`만 복사하면 참조 파일과 계산기가 빠집니다. 저장소 루트나 평가 자료를 활성 스킬로 설치하지 않습니다.

한국어 작성은 [ContextualWisdomLab/korean-writing-skills](https://github.com/ContextualWisdomLab/korean-writing-skills)와 연결합니다. DOCX/PDF 생성은 실행 환경의 문서 스킬을 사용합니다. 이 저장소에 문서 렌더링 엔진이나 ATS 시스템은 포함하지 않습니다.

## 계산과 검증

Python 3.10 이상, 외부 Python 패키지 없이 실행합니다.

```bash
python3 skills/team-lead-resume/scripts/career_months.py periods.json --as-of 2026-10
python3 -m unittest discover -s tests -v
```

입력 스키마와 계산 예시는 [경력 연수 절차](skills/team-lead-resume/references/evidence-workflow.md#3-경력-연수)에 있습니다. 현재 재직은 `end: null`, 포함 여부는 명시적 boolean이며 제외 기록에는 이유가 필요합니다.

계산기는 시작·종료 월을 포함한 월 합집합만 계산합니다. 유관 경력 여부, 시간제 경력의 환산, 정확한 재직 일수, 채용사의 필수 연수 충족을 결정하지 않습니다.

## 근거와 한계

공고 사례는 고용주가 공개한 요구사항입니다. 합격자 원문·입사 결과를 확인한 사례나 시장 전체의 대표 표본이 아닙니다. 대학 지침은 교육 권고, ATS 문서는 해당 제품의 동작 설명이며 서로 같은 근거로 취급하지 않습니다.

실행 검증은 계산 테스트와 소수 합성 과제에 한정합니다. 스킬 없는 기준 응답도 핵심 사실을 이미 보존했습니다. 따라서 일반적인 성능 향상, ATS 점수, 서류 통과율, 채용 성공을 주장하지 않습니다. 실제 지원자의 자료와 기업 시스템에서의 검증은 별도 과제입니다.

개인 이력서·연락처·보상정보·사내 원문을 저장소에 넣지 않습니다. 추가 개발 범위와 미완료 항목은 [제품·기술 Gap 기준선](docs/product-technical-gap-baseline.md)을 참조하세요.
