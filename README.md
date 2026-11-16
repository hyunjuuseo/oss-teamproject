# oss-teamproject
# Legibly
## 1. What it does
legibly는 손글씨 이미지에서 텍스트를 추출하고 읽기 쉽게 정리해 주는 Python 패키지입니다.

사용자가 촬영하거나 저장한 손글씨 이미지를 입력하면 이미지 전처리, 글자 영역 분석, 손글씨 OCR, 텍스트 정리 과정을 거쳐 디지털 텍스트로 변환합니다. 또한 인식이 불확실한 부분은 별도로 표시하여 사용자가 직접 확인하고 수정할 수 있도록 합니다.

주요 기능
- 이미지 전처리: 사진의 기울기, 명암, 그림자 등을 보정하고 잡음을 제거합니다.
- 글자 영역 분석: 이미지에서 텍스트가 있는 영역을 찾아냅니다.
- 손글씨 인식: 한글, 영어, 숫자로 작성된 손글씨를 텍스트로 변환합니다.
- 텍스트 정리: 줄바꿈, 문단, 공백 등을 정돈하여 가독성을 높입니다.
- 불확실 영역 표시: 인식 정확도가 낮은 부분을 별도로 표시합니다.
- 결과 저장: 정리된 텍스트는 TXT 파일로, 불확실한 영역은 JSON 파일로 저장합니다.

대상 사용자
수업 필기나 개인 메모 등을 디지털 문서로 정리하고 싶은 대학생 및 일반 사용자입니다.

개발 목표
손글씨를 일일이 다시 타이핑해야 하는 번거로움을 줄이고, 필기 내용을 보다 쉽고 효율적으로 관리할 수 있도록 하는 것입니다.

## 2. Installation
**요구 사항:** Python 3.9 이상이 필요합니다. 실행에 필요한 Pillow(>= 9.0)는 함께 자동으로 설치됩니다.

#TestPyPI에서 설치하기 (현재)

Legibly는 현재 테스트를 위해 **TestPyPI**에 배포되어 있습니다. 아래 명령어로 설치할 수 있습니다.

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ legibly==0.1.0
```

> `--extra-index-url https://pypi.org/simple/` 옵션은 Pillow 같은 의존성 패키지를 실제 PyPI에서 받아오도록 합니다. TestPyPI에는 이런 패키지가 없을 수 있기 때문입니다.

#PyPI에서 설치하기 (정식 배포 후)

Legibly가 PyPI에 정식으로 배포되면 아래 명령어로 설치할 수 있습니다.

```bash
pip install legibly
```

테스트 도구(pytest)까지 함께 설치하려면 아래 명령어를 사용하세요.

```bash
pip install "legibly[test]"
```

#설치 확인하기

```bash
python -c "import legibly; print('Legibly가 정상적으로 설치되었습니다!')"
```

## 3. Quick start
**설치 확인 (지금 실행 가능).** 설치가 끝났다면 패키지를 import해서 설명을 볼 수 있습니다.

```python
import legibly
help(legibly)
```

**목표 사용법 (개발 중, 아직 동작하지 않음).** 완성되면 필기 사진 한 장에서 정돈된 텍스트 파일까지 아래처럼 만들 수 있게 됩니다.

```bash
legibly lecture.png --output lecture_notes.txt
```

```python
from legibly import restore

result = restore("lecture.png", threshold=0.6)
print(result.text)                 # 정돈된 텍스트
result.save("lecture_notes.txt")
```

위 명령어 이름(`legibly`)과 함수 이름(`restore`)은 [제안서](docs/proposal.md)의 예정 설계이며, 개발하면서 바뀔 수 있습니다. 함수가 구현되면 이 섹션을 실제로 실행되는 예제로 바꿉니다.

## 4. Dependencies
Legibly는 손글씨 이미지의 가독성 개선 및 텍스트 추출을 위한 Python 프로젝트입니다.
현재 핵심 기능을 개발 중이며, 이미지 처리 및 문자 인식에 필요한 라이브러리는 구현 과정에서 확정할 예정입니다.
TODO: 실제 구현에 사용된 라이브러리의 이름, 버전, 용도 및 라이선스를 정리하고 pyproject.toml의 의존성 목록과 일치시키기.

## 5. Tests
TODO

## 6. Documentation
Legibly의 프로젝트 설명과 함수별 API 문서는 MkDocs를 통해 제공됩니다.

- **GitHub Repository:** [https://github.com/hyunjuuseo/oss-teamproject](https://github.com/hyunjuuseo/oss-teamproject)
- **Documentation:** [https://hyunjuuseo.github.io/oss-teamproject/](https://hyunjuuseo.github.io/oss-teamproject/)
- **API Reference:** [https://hyunjuuseo.github.io/oss-teamproject/api/](https://hyunjuuseo.github.io/oss-teamproject/api/)
- **Project Proposal:** [docs/proposal.md](docs/proposal.md)
- **Team Rules:** [docs/team-rules.md](docs/team-rules.md)

각 함수의 매개변수, 반환값, 예외 상황 및 사용 예시는 API 문서에서 확인할 수 있습니다.

문서는 GitHub Actions를 통해 `main` 브랜치의 변경 사항이 자동으로 반영되도록 구성되어 있습니다.


## 7. Release
TODO

## 8. Team
팀원
-  강민채/ ouo417
- 차서현 / chash060919
- 윤채린/ 13ychaelin06
- 서현주 / hyunjuuseo
- 박별 / kpstar1111


팀 협업 규칙
우리 팀은 원활한 협업과 코드 품질 관리를 위해 GitHub Flow를 기반으로 프로젝트를 진행합니다.

- 모든 작업은 기능별 브랜치에서 진행합니다.
- 작업을 시작하기 전에 GitHub Issue를 생성합니다.
- 모든 변경 사항은 Pull Request(PR)를 통해 제출합니다.
- 작성자를 제외한 최소 2명의 팀원이 코드 리뷰를 진행합니다.
- AI 도구를 사용한 경우 PR에 사용 내역을 작성합니다.
- 모든 팀원은 자신이 작성한 코드를 이해하고 직접 테스트해야 합니다.
## 9. License

Legibly 프로젝트는 **MIT License**를 적용할 예정입니다.

MIT License는 저작권 및 라이선스 고지 유지 등의 조건을 준수하는 범위에서 소프트웨어의 사용, 수정 및 재배포를 허용합니다.

정식 라이선스 전문은 저장소 루트의 `LICENSE` 파일에 추가할 예정입니다.
