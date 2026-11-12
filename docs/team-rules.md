# Team Rules (팀 협업 규칙)

> 이 문서는 팀이 합의한 협업 규칙입니다. 모든 팀원과 AI 도구(Claude Code 등)는 이 규칙을 따릅니다.
> 규칙을 바꾸고 싶다면 이 파일을 수정하는 PR을 열고, 정기 회의에서 논의한 뒤 결정합니다.

---

## 1. 작업 흐름 (GitHub Flow)

```
Issue → Branch → Commit → Open PR → Review → Approve → Merge → 브랜치 삭제
```

- **1 Issue = 1 Branch = 1 Pull Request** 원칙을 지킵니다.
- `main`에 **직접 push 하지 않습니다.** 모든 변경은 PR을 거칩니다.
- 작업은 항상 최신 `main`에서 시작합니다.

```bash
git switch main
git pull
git switch -c feat/<기능명>
# ... 작업 및 커밋 ...
git push -u origin feat/<기능명>   # -u는 첫 push에만
```

- 리뷰 반영은 **같은 브랜치에 커밋을 추가로 push** 합니다. 새 PR을 열지 않습니다.
- 이미 push한 커밋은 `rebase`, `reset`, `--force` push 하지 않습니다. 되돌릴 때는 `git revert`를 사용합니다.

---

## 2. PR 크기와 이슈 연동

### 크기
- 하나의 PR에는 **함수 1개 또는 수정 1건**, 즉 단일 기능이나 하나의 수정 사항만 포함합니다.
- 변경량은 **약 100줄 이내**를 권장합니다. 이를 크게 넘으면 PR을 나눕니다.
- 버그 수정, 기능 추가, 이름 변경을 한 PR에 섞지 않습니다.

### 이슈 연동
- 작업을 시작하기 **전에** 관련 GitHub Issue를 먼저 만듭니다.
- PR 본문에 `Closes #이슈번호`를 적어 이슈와 연결합니다.
- 여러 이슈를 닫을 때는 키워드를 **각각** 붙입니다.
  - ✅ `Closes #1, closes #4`
  - ❌ `Closes #1,#4` (→ #1만 닫힘)

### PR 제목
- 형식: `<area>: <대문자로 시작하는 명령형 한 문장>`
- 예: `docs: Add team collaboration rules`, `resize: Keep aspect ratio when only width is given`

### PR 본문 템플릿

```markdown
## What
<!-- 무엇을 바꿨는지 한두 줄 -->

## Why
<!-- 해결하려는 문제, 연결된 이슈의 요구사항 -->

## How
<!-- 구현 방식, 검토했지만 버린 대안과 이유 -->

## How I tested
<!-- 실행한 명령, 입력 → 기대 결과 → 실제 결과, 엣지 케이스 -->

## Open question
<!-- 리뷰어가 먼저 봐야 할 곳 (없으면 None) -->

## AI use
<!-- 도구, 대상 파일/함수, 사용 방식, 직접 검증·수정한 내용. 사용하지 않았으면 none -->

## Checklist
- [ ] 내 diff의 모든 줄을 읽었다
- [ ] 모든 줄을 설명할 수 있다
- [ ] 필요한 경우 README / docstring을 수정했다

Closes #
```

- `## Checklist` 섹션은 **생략할 수 있습니다.** 필수 섹션이 아니며, 스스로 점검하는 용도로 필요할 때만 씁니다.
  - 생략하더라도 작성자는 자기 diff의 모든 줄을 읽고 설명할 수 있어야 합니다. (7장 AI 사용 규칙 참고)
- 그 외 섹션 중 해당 사항이 없는 것은 `None`이라고 적습니다. **`## AI use`는 생략할 수 없습니다.**

---

## 3. 코드 리뷰

### 리뷰어와 기한
- PR 작성자를 **제외한 팀원 최소 2명**이 리뷰합니다.
- 리뷰는 PR이 열린 뒤(또는 리뷰 요청을 받은 뒤) **48시간 이내**에 완료합니다.
- PR을 열 때 **Reviewer를 반드시 지정**합니다. 지정하지 않으면 알림이 가지 않습니다.
- 48시간 안에 리뷰가 어려우면 PR에 댓글로 알리고, 다른 팀원에게 리뷰를 넘깁니다.

### 리뷰 순서
1. Diff를 열기 전에 PR 설명과 연결된 이슈를 읽고, 기대 동작을 한 문장으로 정리합니다.
2. Files changed에서 추가(`+`)와 삭제(`−`)를 모두 읽고, 주변 코드도 확인합니다.
3. 특정 줄에 라인 코멘트를 남기고, 모아서 한 번에 Submit review 합니다.

### 승인 판단: 세 가지 질문

| 질문 | 확인 내용 |
|------|-----------|
| **All of it?** | 이슈의 요구사항을 모두 만족하는가? |
| **Only that?** | 요청하지 않은 동작이 추가되지 않았는가? |
| **Proven?** | 깨지면 실패하는 테스트나 증거가 있는가? |

모두 yes면 **Approve**, 하나라도 no면 **Request changes**.

### 코멘트 접두어 (필수)

| 접두어 | 의미 | 병합 영향 |
|--------|------|-----------|
| `nit:` | 사소한 다듬기 (선택) | 차단 안 함 |
| `suggestion:` | 개선 제안 | 차단 안 함 |
| `question:` | 이유 설명 요청 | 답변 필요 |
| `blocking:` | 병합 전 반드시 수정 | **병합 차단** |

- `blocking:` 코멘트가 달린 경우, **해당 수정 사항을 반영해야만 병합할 수 있습니다.**
- 좋은 코멘트 = 특정 줄/동작 지목 + 왜 중요한지 + 다음에 무엇을 확인할지.
  - 예: `blocking: divide(6, 0) raises ZeroDivisionError. 이슈에서는 None을 반환하라고 했습니다.`

### 리뷰 이후
- **작성자**: 모든 코멘트에 답합니다(수정하거나, 수정하지 않는 이유를 설명). 같은 브랜치에 push 하고 re-review를 요청합니다. 처리된 대화는 Resolve 합니다.
- **리뷰어**: 새 diff를 확인하고, 증거가 불분명하면 로컬에서 직접 재현합니다. blocking이 해결되면 Approve 합니다.
- 리뷰는 사람을 평가하는 것이 아니라 **변경 사항을 읽는 것**입니다. 정중하고 구체적으로 씁니다.

---

## 4. 병합 및 정리

### 병합 조건
- [ ] 작성자를 제외한 **최소 2명의 Approve**
- [ ] 모든 `blocking:` 코멘트 해결
- [ ] 필수 status check(CI) 통과, 충돌 해결

### 병합 절차
- 위 조건을 모두 충족하면, 지정된 리뷰어 중 **마지막으로 Approve 한 사람이** 병합 버튼을 누릅니다.
  - 승인으로 조건이 충족되었다면, 다른 사람을 기다리지 않고 바로 병합합니다.
- 병합 방식은 **`Create a merge commit`** 입니다. (Squash / Rebase merge 사용 안 함)
- 작성자는 자기 PR을 직접 승인하거나 병합하지 않습니다.

### 정리
- 병합이 끝나면 작업 브랜치를 **즉시 삭제**합니다. (GitHub의 *Delete branch* 버튼 + 로컬 삭제)

```bash
git switch main
git pull
git branch -d <브랜치명>
```

- 다른 팀원도 병합 소식을 들으면 `git switch main && git pull`로 로컬 `main`을 갱신합니다.

---

## 5. 브랜치 규칙

- 모든 작업은 `main`이 아닌 **기능별 브랜치**에서 진행합니다.
- 형식을 **엄격히** 지킵니다: `<type>/<설명>` (영문 소문자, 단어는 `-`로 구분)

| 접두어 | 용도 | 예시 |
|--------|------|------|
| `feat/` | 새 기능 | `feat/image-resize` |
| `fix/` | 버그 수정 | `fix/resize-aspect` |
| `docs/` | 문서 (README, `docs/`, docstring) | `docs/team-rules` |
| `chore/` | 설정, 라이선스, 빌드 등 | `chore/license` |

- ❌ `docs.team-rules`, `Feat/Login`, `minchae-work`, `test` 같은 이름은 사용하지 않습니다.
- `gh-pages` 브랜치는 GitHub Actions가 자동 생성하므로 직접 수정하지 않습니다.

---

## 6. 커밋 메시지

- 형식: `<type>: <대문자로 시작하는 명령형 한 줄>`
- 접두어는 브랜치 규칙과 맞춥니다: `feat:`, `fix:`, `docs:`, `chore:`
- **무엇을, 왜** 바꿨는지 씁니다. 어떻게는 코드가 설명합니다.
- 관련 이슈 번호를 끝에 붙입니다.

```text
feat: Add resize() that keeps aspect ratio (#3)
fix: Return None when dividing by zero (#7)
docs: Add team collaboration rules (#1)
chore: Add MIT license (#2)
```

- ❌ 금지: `update`, `fix`, `fix again`, `wip`, `asdf`, `final`, `final2`
- push 전이라면 `git commit --amend`로 메시지를 고칠 수 있습니다. **push 후에는 금지**입니다.
- `git add .` / `git add -A`로 무관한 파일을 한꺼번에 stage 하지 않습니다. 작업과 관련된 파일만 추가합니다.

---

## 7. AI 사용 규칙

### 공개 의무
- **모든 PR**에는 `## AI use` 섹션이 있어야 합니다.
- AI(Claude, ChatGPT, Copilot 등)를 사용한 경우, PR 본문의 **`## AI use` 섹션에 반드시 명시**합니다.
- `## AI use`를 비워 두면 해당 PR의 기여도는 인정되지 않습니다. AI를 쓰지 않았다면 `none`이라고 씁니다.
- 다음 **4가지**를 2~3줄로 적습니다.

| 항목 | 내용 |
|------|------|
| **Tool** | 사용한 도구 (Claude Code, ChatGPT, Copilot …) |
| **Where** | 대상 파일, 함수, 줄 범위 |
| **How** | generated / completed / refactored / explained / reviewed |
| **After** | 사람이 직접 수정·삭제·검증한 내용 |

```markdown
✅ ## AI use
Claude Code generated the first draft of resize() in src/proc.py and
test_resize_width() in tests/test_proc.py. I rewrote the height calculation
(it ignored aspect ratio) and added the height assertion myself.

❌ used ChatGPT
❌ AI helped a bit
```

### 이해 책임
- AI가 작성한 코드는 담당자가 **100% 이해하고 설명할 수 있어야** 합니다. 설명할 수 없는 코드는 PR에 넣지 않습니다.
- 리뷰어는 AI 생성 부분에 대해 `question:`으로 설명을 요청할 수 있고, 작성자는 직접 답해야 합니다.

### PR 전 셀프 체크
1. 코드를 이슈의 요구사항과 대조했다.
2. 일반 입력 1개 + 엣지 케이스 1개 이상으로 직접 실행해 봤다.
3. 사용하는 함수/인자가 현재 라이브러리 버전에 실제로 존재하는지 확인했다.
4. 쓰이지 않는 코드를 지웠다.

### 금지 사항
- AI가 PR을 **승인하거나 병합**하게 하지 않습니다. 승인과 병합은 사람이 합니다.
- 비밀값, 개인정보, 미공개 과제 내용을 외부 AI 서비스에 붙여 넣지 않습니다.

---

## 8. 팀 운영 및 소통

### 정기 회의
- **매주 월요일**에 진행합니다.
- 회의 내용은 그 주의 lab 진행 상황에 따라 정합니다.
- 사전 안건 공유나 회의록 작성은 **필요한 경우에만** 합니다.

### 소통 채널

| 용도 | 채널 |
|------|------|
| 일정 공지, 빠른 질문 | 팀 채팅방 |
| 작업 요구사항 | GitHub Issue |
| 코드 관련 논의 | PR 코멘트 |

- 팀 채팅방 메시지에는 **24시간 이내**에 응답합니다.

### 문제 발생 시 조치
- 개발 중 오류가 생기거나 일정이 지연될 것 같으면 **즉시 팀 채팅방에 공유**합니다. 혼자 오래 붙잡고 있지 않습니다.
  - 공유할 때: 무엇을 하려 했는지 / 무엇이 일어났는지 / 재현 방법 / 시도해 본 것
- 마감 **2일 전까지** 완료가 어렵다고 판단되면 팀 채팅방에 알리고 작업을 나누거나 재배정합니다.
- 의견 충돌이 생기면 각자 **이유를 적어** 논의하고, 합의되지 않으면 **다수결**로 결정합니다.
  - PR 리뷰에서 2라운드 이상 해결되지 않는 충돌은 정기 회의 안건으로 올립니다.

---

## 9. 이슈 관리

- 제목만 보고도 무슨 일인지 알 수 있게 한 줄로 씁니다. (❌ `Bug`, `수정`)
- 이슈를 열 때 **Assignee**를 지정하고, 담당자는 `I will take this` 등의 댓글을 남깁니다.
- **Label**을 붙입니다: `bug`, `enhancement`, `documentation`, `question`, `good first issue`
- **Milestone**으로 목표 버전(예: `v0.1.0`)을 묶습니다.
- 요구사항이 모호하면 코드를 쓰기 **전에** 이슈에서 먼저 명확히 합니다.
- 모든 이슈에는 **완료 기준(Done when)** 을 적습니다.

### 기능 요청 템플릿
```markdown
## Problem
## Proposed change
## Alternatives considered
## Done when
```

### 버그 리포트 템플릿
```markdown
## Expected behavior
## Actual behavior
## Steps to reproduce
1.
2.
## Environment
<!-- OS, Python 버전, 라이브러리 버전 -->
```

---

## 10. 보안 및 저장소 위생

- **비밀값(API key, token, password)은 절대 커밋하지 않습니다.** 환경 변수나 `.env`(커밋 제외)를 사용합니다.
- 키가 실수로 커밋되었다면 파일 삭제로는 해결되지 않습니다. **즉시 팀에 알리고 키를 폐기·재발급**합니다.
- 다음은 `.gitignore`에 포함하고 커밋하지 않습니다.
  - `.venv/`, `__pycache__/`, `.pytest_cache/`, `node_modules/`
  - `.vscode/`, `.idea/`, `.DS_Store`
  - `.env`, 대용량 데이터, 바이너리, 빌드 산출물

---

## 11. 테스트와 문서화

- 새 기능이나 버그 수정에는 **가능한 한 테스트를 함께** 추가합니다. 테스트 방법은 PR의 `## How I tested`에 적습니다.
- 함수에는 **Google style docstring**을 작성합니다. (요약줄, Args, Returns, Raises, Examples)
- 동작을 바꾸는 PR은 **같은 PR에서** README / docstring도 함께 수정합니다.
- 새 문서 페이지는 `docs/<name>.md`로 추가하고, `mkdocs.yml`의 `nav`에 한 줄을 추가합니다.
---

*마지막 수정: 2026-11-11*
