# 프로젝트 제안서(Project proposal): "프로젝트 이름(Project name)"

## 1. 프로젝트 주제(Project topic)

### 만들고 싶은 프로그램(What we want to build)

> 어떤 프로그램을 개발할지 한두 문장으로 설명. (Describe the program you want to build in one or two sentences.)

> 예시(Example): 비디오에 등장하는 사람의 얼굴을 검출하고, 검출한 얼굴 영역을 흐리게 처리한 새 영상을 저장하는 Python 패키지를 개발.
> (We will build a Python package that detects faces in a video, blurs the detected face regions, and saves a new video.)

### 사용자 정의 및 해결할 문제(Users and problem)

> 누가, 어떤 상황에서 이 프로그램을 사용하는가? 사용자가 겪는 문제와 이 프로그램이 필요한 이유를 설명. (Explain who will use the program, when they will use it, and what problem it will help them solve.)

> 예시(Example): 동아리 소개 영상을 만드는 학생은 촬영된 사람의 얼굴을 가리기 위해 영상 편집기에서 같은 작업을 반복. 이 프로그램은 검출한 얼굴에 블러를 적용해 반복 편집 작업을 줄여 준다.
> (Students making club introduction videos repeatedly cover faces in a video editor. This program will reduce that repetitive editing by applying blur to detected faces.)

## 2. 개발할 기능(Planned features)

### 입력(Input)

> 사용자가 제공하는 데이터와 형식 정의 (Describe the data users will provide and its format.)

> 예시(Example): 사용자가 컴퓨터에 저장한 MP4 영상 파일을 입력
> (The user provides an MP4 video file stored on their computer.)

### 처리(Processing)

> 입력을 받은 뒤 프로그램이 수행할 구체적인 작업을 정의. “AI로 처리한다”처럼 모호하게 쓰지 말고, 실제로 개발할 동작을 설명.> (List the specific tasks program will perform. Explain the behavior you will implement rather than using vague descriptions such as “process it with AI.”)

> 예시(Example):
> 1. 입력 영상을 프레임별로 읽기(Read the input video frame by frame).
> 2. 각 프레임에서 사람의 얼굴 영역을 검출(Detect human face regions in each frame).
> 3. 검출한 얼굴 영역에 블러를 적용(Apply blur to the detected face regions).
> 4. 처리한 프레임을 순서대로 연결해 새 MP4 영상으로 저장(Save the processed frames in order as a new MP4 video).

### 결과(Output)

> 사용자가 받게 될 결과물이 무엇인지 설명. 파일이라면 형식과 주요 특징도 기술. (Describe the result users will receive. If it is a file, specify its format and main characteristics.)

> 예시(Example): 검출한 얼굴이 흐리게 처리된 새 MP4 파일을 저장. 원본은 보존하며, 결과 영상은 원본과 같은 해상도와 재생 속도(fps)를 유지. 이번 개발 범위에서는 오디오를 포함하지 않는다.
> (The program saves a new MP4 file with detected faces blurred. It preserves the original file and keeps the original resolution and frame rate. Audio is outside the scope of this project.)

### 개발 범위(Scope)

> - 포함할 기능(In scope): <이번 프로젝트에서 구현할 기능 예시>
> - 제외할 기능(Out of scope): <이번 프로젝트에서 지원하지 않을 기능 예시>

> 예시(Example):
> - 포함할 기능(In scope): 저장된 MP4 읽기, 얼굴 검출, 블러 처리, 새 MP4 저장(Reading stored MP4 files, detecting faces, applying blur, and saving a new MP4).
> - 제외할 기능(Out of scope): 실시간 웹캠 처리, 특정 인물 식별, 오디오 보존(Live webcam processing, identifying specific people, and preserving audio).
> - 한계(Limitation): 검출하지 못한 얼굴은 블러 처리되지 않을 수 있으므로 결과 영상을 직접 확인해야한다.(Undetected faces may remain visible, so the output video must be checked manually).

### 사용 예시(Usage example)

> 사용자가 입력을 준비하고 프로그램을 사용해 결과를 얻는 한 가지 상황을 예시로 설명. 실제 파일이나 실행 결과를 제출할 필요는 없음. (Describe one scenario from preparing the input to receiving the output. You do not need to submit an actual input file or execution result today.)

> 예시(Example): 학생이 5초 길이의 동아리 소개 영상 `club.mp4`를 입력. 프로그램은 각 프레임에서 검출한 얼굴을 흐리게 처리하고, 무음 영상 `club_blurred.mp4`를 새로 저장. 학생은 결과 영상을 재생하며 얼굴 검출이 누락된 부분이 있는지 확인.
> (A student provides a five-second club introduction video, `club.mp4`. The program blurs detected faces in each frame and saves a new silent video, `club_blurred.mp4`. The student plays the output and checks for any missed faces.)
