# Meetifyr 프로젝트

# 개발 환경 구축

1. poetry
2. black
3. ruff
4. git init
5. mypy

## 1. poetry 설치 및 설정

1. poetry
2. poetry init
3. poetry lock
4. poetry add fastapi

## 2. black 설치 및 설정

> formater

1. poetry add --group=dev black==24.10.0
2. 실행해보기
   `poetry run black .`

## 3. ruff

> formater + linter

1. poetry add --group=dev ruff=0.8.2
2. `#noqa` 주석을 달면 그냥 지나감

## 4. git

## 5. MyPy

1. poetry add --group=dev mypy=1.13.0
2. mypy .

# 테스트 환경 구축

1. pytest 설치
   `poetry add --group=dev pytest==8.3.4`

2. 간단 테스트
   `pytest .`

3. 테스트 방식
   Given > When > Then

4. coverage 설치

> 단위별 테스트

`poetry add --group=dev coverage==7.6.9`
`poetry run coverage run -m pytest temp.py`
`poetry run coverage report -m`
`poetry run coverage html`

5. omit 설정

> coverage에선 testcode는 들어가지 않음 제품 코드만 들어가야함. -> omit
> 제품 코드와 테스트 코드 분리

6. 의존성(종속성) 관리

- dev dependency
  지금까지 `group=dev` 를 사용해서 라이브러리들을 설치하였습니다. 이 `group=dev` 는 어떤 의미일까요?

  - `pyproject.toml`

    ```

    [tool.poetry.dependencies]
    python = "^3.13"
    fastapi = "^0.115.6"
    uvicorn = "^0.32.1"

    [tool.poetry.group.dev.dependencies]
    black = "24.10.0"
    ruff = "0.8.2"
    mypy = "1.13.0"
    pytest = "8.3.4"
    coverage = "^7.6.9"
    pytest-asyncio = "^0.25.0"

    ```

    종속성은 2가지로 나눌 수 있습니다.

  - 서버가 실행되는 중에 필요한 종속성 (예: fastapi, uvicorn, pydantic)
  - 개발하는 중에만 필요하고, 서버가 실행되는 도중에는 전혀 사용되지 않는 종속성
    `group=dev` ”이 종속성은 개발할때만 필요하고, 서버가 실행될 때에는 필요하지 않다” 라는 의미입니다.
    따라서 지금까지 black, ruff, mypy, pytest, coverage 등을 모두 `dev` group 으로 지정하여 설치하였습니다.
    이렇게 종속성을 분리해서 관리하면 프로덕션 환경에서 “쓰지 않을 종속성”을 설치하느라 시간과 공간을 낭비할 필요가 없어집니다.
    특히 ec2 환경보다는 docker 환경에서(kubernetes) 종속성 분리가 빛을 발합니다.
  - 매번 업데이트 시마다 docker 이미지를 새로 빌드하는데, 이미지 사이즈 자체가 줄어드니 저장 비용이 감소합니다.
  - 매번 배포 시마다 새 이미지를 다운받고 실행하는데, 이때도 사이즈가 작으면 더 빠르게 배포할 수 있습니다.
    dev group 을 제외하고 설치를 하려면 `poetry install --no-root --only main` 을 하면 됩니다.
  - no-root: poetry 기본 설정은 프로젝트를 어플리케이션이(회사가 직접 사용할 서버 등등. 다른 사람이 가져가라고 만든 것이 아님) 아니라 라이브러리(다른 사람이 가져다 쓸 수 있도록 만든 프로그램)로 간주하는데요, `no-root` 옵션을 사용해야 어플리케이션으로 인식해서 자기 자신(root)을 설치하지 않습니다. (참고: https://python-poetry.org/docs/cli/#options-2)
  - only main: dev group 이 아닌 main 그룹만 설치하겠다는 의미입니다.

7. asyncio 설치
   `poetry add --group dev pytest-asyncio`
   ``

# 미팅 생성 API 스펙 만들기

## 첫번째 api 미팅 생성

다음 파일들을 생성합니다.

1. app 생성 /
2. asgi 생성
3. poetry add orjson==3.10.12
4. unicorn 설치
5. createMeetingResponse 생성
6. frozen_config 생성
7. 라우터 만들기

- 실제 배포 시에도 사용하므로 ! dev==group

- `app/__init__.py`

  ```python
  from fastapi import FastAPI
  from fastapi.responses import ORJSONResponse

  app = FastAPI(
      default_response_class=ORJSONResponse
  )
  ```

- `asgi.py`

  ```python
  from app import app

  if __name__ == "__main__":
      import uvicorn

      uvicorn.run(app, host="0.0.0.0", port=8000)
  ```

## 미팅 생성 spec_swagger

DTO(Data Transfer Object)

> 데이터를 전달하기 위한 목적으로 생성된 객체
> DTO는 오직 데이터를 '전달'만 해야하며, 데이터를 수정, 추가, 삭제하면 안됨.

## uuid4, base64 이용하여 랜덤 생성

> 고유식별자

- uuid: 랜덤
- base64, base62: 변환 알고리즘

### Deterministic

Base62의 연산은 결정적이다. > 결과값이 정해져있다.

## Sqids

> 숫자로부터 짧은 고유 식별자 생성하는 라이브러리

- `poetry add sqids`

# DB 개발 및 테스트 자동화.

## EdgeDB

## MySQLDB

1. 기본 라이브러리 설치
2. base_config.py 작성
3. tortoise_config.py 작성

### 1. 기본 라이브러리 설치

`poetry add "tortoise-orm[asyncmy]==0.23.0"`
`poetry add cryptography==44.0.0`
`poetry add aerich==0.8.1 tomlkit==0.13.2`
`poetry add pydantic_settings==2.7.1`

### 2. base config.py

```
from enum import StrEnum
from pydantic_settings import BaseSettings

class Env(StrEnum):
LOCAL = "local"
STAGE = "stage"
PROD = "prod"

class Config(BaseSettings):
ENV: Env = Env.LOCAL

MYSQL_HOST: str = "localhost"
MYSQL_PORT: int = 3306
MYSQL_USER: str = "root"
MYSQL_PASSWORD: str = "1234"
MYSQL_DB: str = "when2meet_vod"
```

### 3. tortoise_config.py

```
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.configs import config

TORTOISE_APP_MODELS = [
    "app.tortoise_models.meeting",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": { # 접속 정보
                "host": config.MYSQL_HOST,
                "port": config.MYSQL_PORT,
                "user": config.MYSQL_USER,
                "password": config.MYSQL_PASSWORD,
                "database": config.MYSQL_DB,
                "connect_timeout": 5,
                "maxsize": 30,
            },
        },
    },
    "apps": {
        "models": {
            "models": TORTOISE_APP_MODELS,
        },
    },
    "timezone": "Asia/Seoul",
}


def initialize_tortoise(app: FastAPI) -> None:
    Tortoise.init_models(TORTOISE_APP_MODELS, "models")
    register_tortoise(app, config=TORTOISE_ORM)
```

### 4. tortoise_models/base_model.py

```
from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)
```

## tortoise_models/meetings.py

1. meeting.py 작성
2. aerich 사용한 DB 생성

### 1. meeting.py

```
from __future__ import annotations # __future__: 미래의 버전의 것을 불러오는 것, annotations > 문자열로 안바꿔도 인식
from tortoise import Model, fields
from app.tortoise_models.base_model import BaseModel

class MeetingModel(BaseModel, Model):
  url_code = fields.CharField(max_length=255, unique=True)

  class Meta:
    table = "meetings"

  # 응집성, 쿼리를 모아둬야 나중에 조사할 때, 필요함.
  @classmethod
  async def create_meeting(cls, url_code:str) -> MeetingModel:
    return await cls.create(url_code=url_code)
```

### 2. aerich 사용하여 DB 생성

`aerich init -t app.configs.tortoise_config.TORTOISE_ORM`
`aerich init-db` #migration

- aerich <-> Alembic
  > aerich는 DB를 바꿀 때, 많은 코드를 바꿔야함
  > Alembic은 Query를 바꿀 때, 많은 코드를 바꿔야함.

## PyTest, Tortoise-ORM을 활용한 TestCode 작성

1. conftest.py 작성
2. `poetry add httpx==0.28.1`
3. app/tests/apis/v1/test_meeting_router_mysql.py

### 1. conftest.py 작성

```
import asyncio
from typing import Any, Generator
from unittest.mock import Mock, patch

import pytest
import pytest_asyncio
from pytest import FixtureRequest
from tortoise.backends.base.config_generator import generate_config
from tortoise.contrib.test import finalizer, initializer

from app.configs import config
from app.configs.tortoise_config import TORTOISE_APP_MODELS

TEST_BASE_URL = "http://test"
TEST_DB_LABEL = "models"
TEST_DB_TZ = "Asia/Seoul"


def get_test_db_config() -> dict[str, Any]:
    tortoise_config = generate_config(
        db_url=f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/test",
        app_modules={TEST_DB_LABEL: TORTOISE_APP_MODELS},
        connection_label=TEST_DB_LABEL,
        testing=True,
    )
    tortoise_config["timezone"] = TEST_DB_TZ

    return tortoise_config


@pytest.fixture(scope="session", autouse=True)
def initialize(request: FixtureRequest) -> Generator[None, None]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with patch("tortoise.contrib.test.getDBConfig", Mock(return_value=get_test_db_config())):
        initializer(modules=TORTOISE_APP_MODELS)
    yield
    finalizer()
    loop.close()


@pytest_asyncio.fixture(autouse=True, scope="session")
def event_loop() -> None:
    pass

```

### 2. `poetry add httpx==0.28.1`

### 3. app/tests/apis/v1/test_meeting_router_mysql.py

```
import httpx
from starlette.status import HTTP_200_OK
from tortoise.contrib.test import TestCase

from app import app


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_mysql(self) -> None:
        # When
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.post(url="/v1/mysql/meetings")

        # Then: 테스트 결과를 검증
        assert response.status_code == HTTP_200_OK


```

# Edge DB와 MySQL로 구현하는 조건 기반 미팅 기능

1. meeting의 조회와 요구사항
2. dmypy
3. metting api 스펙 생성
4. Tortoise-ORM으로 Meeting 조회 테스트 작성 및 API 구현
5. MySQL Query Log 조회하기

## meeitng의 조회와 요구사항

1. 실시간 응답 > websocekt 사용. > meeting 조회 API를 생성 http polling은 비효율적
2. 요청시마다 주고 받는 오버헤드 줄이기 위해 daemon 사용

## dmypy 사용하기

test.sh
`poetry run dmypy run -- .`

## meeting api 스펙 생성

meeting_router.py

```
from app.dtos.get_meeting_response import GetMeeetingResponse

@edgedb_router.get(
    "/{meeting_url_code}", # path variable 문법
    description="meeitng을 조회합니다."
)
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeeetingReponse
    return GetMeeetingReponse(url_code="abc")
```

## Tortoise-ORM으로 Meeting 조회 테스트 작성 및 API 구현

tortoise_models/meeting.py

```
@classmethod
async def get_by_url_code(cls, url_code: str) -> MeetingModel | None:
    return await cls.filter(url_code=url_code).get_or_None()
```

## MySQL QueryLog 조회하기

## Meeting 날짜 업데이트 요구사항

1. 4주 후, 이번 달, 다음 달 중에서 고를 수 있고, Select dates 로 직접 지정할 수도 있습니다.

- 시작 날짜보다 종료 날짜가 더 뒤인지 검증
- 기간을 최대 62일로 제한
- 기간을 한 번 정하면 바꿀 수 없도록 제한

## 날짜 업데이트 시작!

서순

1. dto 만들기
2. router

### dto/update_meeting_request.py

```
from datetime import date, timedelta
```

## Meetings.models.py 수정

1. 쿼리 구현
2. 테스크 케이스 추가
3. 서비스 작성
4. 라우터 작성
5. 추가 테스트 (이미 미팅이 생성되어 있거나 , 찾지 못한 경우)

## 제목 수정 api와 제목 수정 api

meetings_router.py

```
@edgedb_router.patch(
    "/{meeting_url_code}/title",
    description="meeting 의 title 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_title_edgedb(
    meeting_url_code: str, update_meeting_title_request: UpdateMeetingTitleRequest
) -> None:
    return None


@mysql_router.patch(
    "/{meeting_url_code}/title",
    description="meeting 의 title 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_title_mysql(
    meeting_url_code: str, update_meeting_title_request: UpdateMeetingTitleRequest
) -> None:
    return None


@edgedb_router.patch(
    "/{meeting_url_code}/location",
    description="meeting 의 location 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_location_edgedb(
    meeting_url_code: str, update_meeting_location_request: UpdateMeetingLocationRequest
) -> None:
    return None


@mysql_router.patch(
    "/{meeting_url_code}/location",
    description="meeting 의 location 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_location_mysql(
    meeting_url_code: str, update_meeting__location_request: UpdateMeetingLocationRequest
) -> None:
    return None

```

## Location MySQL Query 작성

# 참가자 관리 및 일정 기능 API 개발

## 참가자 생성 기능의 요구사항

### 날짜 데이터, 어떻게 할 것인가??

이 날짜 데이터를 어떻게 기록하면 좋을까요?

- 참가자 생성 시점에 날짜 데이터를 전부 생성한 뒤, True 와 False 로 둘 수도 있고
  - e.g.) 1월 20 ~ 23일 이라면 데이터베이스 테이블 `dates` 에 `{"date": "2024-01-20" "free": True, starred: False, "participant": "참가자1"}` 의 형상을 가진 row 4개가 생성됨.
- 별 표, busy 체크가 된 경우에만 row 를 생성하도록 할 수도 있습니다. (이 경우 해당 날짜에 busy 체크가 되어있다면 별표 생성을 못하도록 막아야 합니다.) busy 가 없는 날을 전부 Free 로 계산해서 클라이언트에게 보여주어야 합니다.
  - e.g.) 1월 20 ~ 23 이고 21에 star가 있고 22일만 busy 라면
    - `star` 테이블 `{"date": "2024-01-21" "participant": "참가자1"}`
    - `busy` 테이블 `{"date": "2024-01-22" "participant": "참가자1"}`
    - 나머지는 자동으로 일반 Free (meeting 의 start 와 end 를 알 수 있으니까 나머지 free 날짜를 구할 수 있습니다.)

저장의 효율성 측면에서 후자가 낫지만, 전자가 로직이 심플하기 때문에 전자를 선택하겠습니다.

## 참가자 생성 mock api 생성

1. app/dtos/create_participant_request.py

```
from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateParticipantRequest(BaseModel):
    model_config = FROZEN_CONFIG

    meeting_url_code: str
    name: str

```

2. app/dtos/create_participant_response.py

```
import datetime
import uuid

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class ParticipantDateMysql(BaseModel):
    model_config = FROZEN_CONFIG
    id: int
    date: datetime.date


class CreateParticipantMysqlResponse(BaseModel):
    model_config = FROZEN_CONFIG
    participant_id: int
    participant_dates: list[ParticipantMysql]



class ParticipantDateEdgedb(BaseModel):
    model_config = FROZEN_CONFIG
    id: uuid.UUID
    date: datetime.date


class CreateParticipantEdgedbResponse(BaseModel):
    model_config = FROZEN_CONFIG
    participant_id: uuid.UUID
    participant_dates: list[ParticipantEdgedb]

```

3. app/apis/v1/participant_router.py

```
from fastapi import APIRouter

from app.dtos.create_participant_request import (
    CreateParticipantRequest,
)
from app.dtos.create_participant_response import (
    CreateParticipantMysqlResponse,
)

mysql_router = APIRouter(
    prefix="/v1/mysql/participants",
    tags=["Participant"],
)


@mysql_router.post(
    "", description="participant 를 생성합니다."
)
async def api_create_participant_mysql(
    create_participant_request: CreateParticipantRequest,
) -> CreateParticipantMysqlResponse:
    return CreateParticipantMysqlResponse(
        participant_id=123, participant_dates=[]
    )
```

4. **init**.py

```
from app.apis.v1.participant_router import (
    mysql_router as participant_mysql_router,
)

app.include_router(participant_mysql_router)
```

## Participant, ParticipantDate Model의 마이그레이션

### 테스트

- `app/tests/apis/v1/test_participant_router_mysql.py`

  ```

  import datetime

  import httpx
  from starlette.status import (
      HTTP_200_OK,
      HTTP_400_BAD_REQUEST,
      HTTP_404_NOT_FOUND,
  )
  from tortoise.contrib.test import TestCase

  from app import app
  from app.tortoise_models.participant import ParticipantModel
  from app.tortoise_models.participant_date import ParticipantDateModel

  class TestParticipantRouter(TestCase):
      async def test_api_create_participant_mysql(self) -> None:
          async with httpx.AsyncClient(
              transport=httpx.ASGITransport(app=app),
              base_url="http://test",
          ) as client:
              # Given
              meeting_create_response = await client.post("/v1/mysql/meetings")
              url_code = meeting_create_response.json()["url_code"]

              await client.patch(
                  f"v1/mysql/meetings/{url_code}/date_range",
                  json={"start_date": "2025-10-10", "end_date": "2025-10-12"},
              )

              # When
              response = await client.post(
                  "/v1/mysql/participants",
                  json={"meeting_url_code": url_code, "name": (participant_name := "test")},
              )

          # Then
          self.assertEqual(response.status_code, HTTP_200_OK)
          response_body = response.json()
          participant = await ParticipantModel.filter(id=response_body["participant_id"]).get()
          self.assertEqual(participant_name, participant.name)
          self.assertEqual(url_code, participant.meeting_id)
          participant_dates = await ParticipantDateModel.get_all_by_participant_id(participant.id)
          self.assertEqual(len(participant_dates), 3)
          self.assertEqual(
              [date.date for date in participant_dates],
              [datetime.date(2025, 10, 10), datetime.date(2025, 10, 11), datetime.date(2025, 10, 12)],
          )

      async def test_can_not_create_participant_when_meeting_does_not_exist(self) -> None:
          # When
          async with httpx.AsyncClient(
              transport=httpx.ASGITransport(app=app),
              base_url="http://test",
          ) as client:
              # When
              response = await client.post(
                  "/v1/mysql/participants",
                  json={"meeting_url_code": "not_exist", "name": "test"},
              )

          # Then
          self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
          response_body = response.json()
          self.assertEqual(response_body["detail"], "meeting with url_code: not_exist not found")

      async def test_can_not_create_participant_when_meeting_date_range_does_not_exist(self) -> None:
          # When
          async with httpx.AsyncClient(
              transport=httpx.ASGITransport(app=app),
              base_url="http://test",
          ) as client:
              # Given
              meeting_create_response = await client.post("/v1/mysql/meetings")
              url_code = meeting_create_response.json()["url_code"]

              # When
              response = await client.post(
                  "/v1/mysql/participants",
                  json={"meeting_url_code": url_code, "name": "test"},
              )

          # Then
          self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
          response_body = response.json()
          self.assertEqual(response_body["detail"], "start and end should be set.")

  ```

### 서비스 구현

- `app/services/participant_service_mysql.py`

  ```python
  from datetime import date, timedelta

  from tortoise.transactions import in_transaction

  from app.dtos.create_participant_request import CreateParticipantRequest
  from app.tortoise_models.participant import ParticipantModel
  from app.tortoise_models.participant_date import ParticipantDateModel

  async def service_create_participant(
      create_participant_request: CreateParticipantRequest,
      meeting_start_date: date,
      meeting_end_date: date,
  ) -> tuple[ParticipantModel, list[ParticipantDateModel]]:
      dates = [meeting_start_date + timedelta(days=i) for i in range((meeting_end_date - meeting_start_date).days + 1)]
      async with in_transaction():
          participant = await ParticipantModel.create_participant(
              name=create_participant_request.name,
              meeting_url_code=create_participant_request.meeting_url_code,
          )
          await ParticipantDateModel.bulk_create_participant_date(
              participant_id=participant.id,
              dates=dates,
          )
          participant_dates = await ParticipantDateModel.get_all_by_participant_id(participant.id)
      return participant, participant_dates

  ```

- 2번 이상의 insert 쿼리를 하므로, transaction 으로 묶어줍니다.
- (트랜젝션은 일련의 쿼리를 “모두가 다 성공하거나, 모두가 다 실패하도록” 만들어줍니다.
- 트랜젝션의 이러한 특성을 `Atomicity` 원자성 이라고 합니다.
- Tortoise 공식 문서의 가이드대로 `in_transaction()` 을 사용해서 트랜젝션을 사용하겠습니다.
  https://tortoise.github.io/transactions.html

## 멱등성

> 같은 작업을 여러번 수행해도 최종결과가 같은 특성
