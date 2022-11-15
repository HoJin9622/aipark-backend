# :test_tube: aipark-backend

TTS 딥러닝 모델을 사용하기 위한 기능 서버

## :scroll: 목차

- [:test_tube: aipark-backend](#test_tube-aipark-backend)
  - [:scroll: 목차](#scroll-목차)
  - [:notebook_with_decorative_cover: 프로젝트 요구사항](#notebook_with_decorative_cover-프로젝트-요구사항)
  - [:whale: Development(Docker)](#whale-developmentdocker)
  - [:mag_right: Development(Poetry)](#mag_right-developmentpoetry)
  - [:pencil2: Commit Message Convention](#pencil2-commit-message-convention)
  - [:chart_with_upwards_trend: Git Flow / Branch Information](#chart_with_upwards_trend-git-flow--branch-information)
  - [:closed_book: API Docs](#closed_book-api-docs)
    - [프로젝트 생성](#프로젝트-생성)
    - [텍스트 조회](#텍스트-조회)
    - [텍스트 수정](#텍스트-수정)
    - [텍스트 생성](#텍스트-생성)
    - [텍스트 삭제](#텍스트-삭제)
    - [프로젝트 삭제](#프로젝트-삭제)

## :notebook_with_decorative_cover: 프로젝트 요구사항

1. Text to Speech(TTS) 딥러닝 모델을 사용하기 위한 일부 기능을 구현하는 과제입니다.
2. 다음 기능을 수행하는 테이블을 설계, 구축하고, 이를 기반으로 REST API 서버를 개발합니다

- 프로젝트 생성(오디오 생성)
  - 텍스트(str)가 담긴 리스트를 받습니다. (length = 1)
  - 이를 전처리하여 오디오를 생성하는 함수의 input으로 같이 넣습니다.
    [['text1', 'text2', 'text3', ....], path]
  - 일정시간 이후 함수에서 (id, text)형태의 원소를 가진 리스트를 리턴합니다.
    [('id1' ,'text1'), ('id2', 'text2'), ('id3', 'text3'), ....]
  - 오디오는 input의 path에 저장됩니다.
- 텍스트 조회
  - 특정 프로젝트의 n번째 페이지를 조회합니다.
  - 한페이지는 10문장으로 이루어져 있습니다.
- 텍스트 수정
  - 한 문장의 텍스트와 스피드를 수정합니다.
- 오디오파일 송신
  - 요청받은 오디오파일을 송신합니다.
- 텍스트(오디오) 생성 / 삭제
  - 삽입위치는 항상 앞, 뒤가 아닌 중간도 가능.
- 프로젝트 삭제

## :whale: Development(Docker)

```bash
# Application Run
docker-compose up
```

## :mag_right: Development(Poetry)

```bash
# 가상환경 진입
poetry shell

# 관련 패키지 설치
poetry install

# Application Run
python manage.py runserver
```

## :pencil2: Commit Message Convention

- feat: 기능 추가, 삭제, 변경(or ✨ emoji) - 제품 코드 수정 발생
- fix: 버그 수정(or 🐛 emoji) - 제품 코드 수정 발생
- docs: 문서 추가, 삭제, 변경(or 📝 emoji) - 코드 수정 없음
- style: 코드 형식, 정렬, 주석 등의 변경, eg; 세미콜론 추가(or 💎 emoji) - 제품 코드 수정 발생, 하지만 동작에 영향을 주는 변경은 없음
- refactor: 코드 리펙토링, eg. renaming a variable(or ♻️ emoji) - 제품코드 수정 발생
- test: 테스트 코드 추가, 삭제, 변경 등(or 🧪 emoji) - 제품 코드 수정 없음. 테스트 코드에 관련된 모든 변경에 해당
- chore: 위에 해당하지 않는 모든 변경(or 🧹 emoji), eg. 빌드 스크립트 수정, 패키지 배포 설정 변경 - 코드 수정 없음

위 규칙에 맞게 커밋메시지를 작성한다.

## :chart_with_upwards_trend: Git Flow / Branch Information

```
- main: 제품으로 출시 될 수 있는 브랜치입니다.
- develop: 다음 출시 버전을 개발합니다.
- feature: 다가오는 배포(release)를 위한 새 기능(feature)을 개발합니다.
- release: 새로운 제품 출시 준비를 지원합니다.
- hotfix: 핫픽스는 현재 출시된 제품에 문제가 생겨서 즉각 대응해야하는 상황에서 필요합니다.
```

## :closed_book: API Docs

### 프로젝트 생성

| Method | URL              | Description                             |
| ------ | ---------------- | --------------------------------------- |
| POST   | api/v1/projects/ | 프로젝트를 생성 후 오디오를 생성합니다. |

- Request Example

  ```json
  {
    "text": "Hello! How are you?", // required
    "audio_index": 1, // required
    "title": "테스트 프로젝트" // required
  }
  ```

- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 텍스트 조회

| Method | URL                          | Description                           | Query Parameter |
| ------ | ---------------------------- | ------------------------------------- | --------------- |
| GET    | api/v1/projects/{id}/audios/ | 해당 id의 텍스트를 목록을 조회합니다. | page            |

- Response Example
  ```json
  [
    {
      "id": 4,
      "create_time": "2022-11-15T23:27:31.864274+09:00",
      "update_time": "2022-11-15T23:27:31.864296+09:00",
      "index": 2,
      "text": "wow! awesome! it's so great.",
      "speed": 3,
      "path": "files/2.mp3",
      "processed_text": ["wow", "awesome", "it's so great"]
    }
  ]
  ```

### 텍스트 수정

| Method | URL                 | Description                        |
| ------ | ------------------- | ---------------------------------- |
| PATCH  | api/v1/audios/{id}/ | id에 해당하는 텍스트를 수정합니다. |

- Request Example

  ```json
  {
    "text": "Hello! How are you?", // optional
    "speed": 1 // optional
  }
  ```

- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 텍스트 생성

| Method | URL                          | Description          |
| ------ | ---------------------------- | -------------------- |
| POST   | api/v1/projects/{id}/audios/ | 텍스트를 생성합니다. |

- Request Example

  ```json
  {
    "text": "Hello! How are you?", // required
    "speed": 1, // required
    "index": 1 // required
  }
  ```

- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 텍스트 삭제

| Method | URL                 | Description          |
| ------ | ------------------- | -------------------- |
| DELETE | api/v1/audios/{id}/ | 텍스트를 삭제합니다. |

- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 프로젝트 삭제

| Method | URL                   | Description            |
| ------ | --------------------- | ---------------------- |
| DELETE | api/v1/projects/{id}/ | 프로젝트를 삭제합니다. |

- Response Example
  ```json
  {
    "ok": true
  }
  ```
