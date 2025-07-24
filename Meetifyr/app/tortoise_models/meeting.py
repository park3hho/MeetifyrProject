from __future__ import (
    annotations,
)  # __future__: 미래의 버전의 것을 불러오는 것, annotations > 문자열로 안바꿔도 인식

from datetime import date
from typing import TYPE_CHECKING

from tortoise import Model, fields

from app.tortoise_models.base_model import (
    BaseModel,
)

if TYPE_CHECKING:
    from app.tortoise_models.participant import (
        ParticipantModel,
    )


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(
        max_length=255, unique=True
    )
    title = fields.CharField(
        max_length=255, default=""
    )
    location = fields.CharField(
        max_length=255, default=""
    )
    start_date = fields.DateField(null=True)
    end_date = fields.DateField(null=True)
    participants: list[ParticipantModel]

    class Meta:
        table = "meetings"

    # 응집성, 쿼리를 모아둬야 나중에 조사할 때, 필요함.

    # 데이터 베이스를 접근하기 위한 클래스메소드 생성(격식 확인용)
    @classmethod
    async def create_meeting(
        cls, url_code: str
    ) -> MeetingModel:
        return await cls.create(url_code=url_code)

    @classmethod  # 추가
    async def get_by_url_code(
        cls, url_code: str
    ) -> MeetingModel | None:
        return (
            await cls.filter(url_code=url_code)
            .prefetch_related(
                "participants",
                "participants__participant_dates",
            )
            .get_or_none()
        )

    @classmethod
    async def update_start_and_end(
        cls,
        url_code: str,
        start_date: date,
        end_date: date,
    ) -> None:
        await cls.filter(
            url_code=url_code
        ).update(
            start_date=start_date,
            end_date=end_date,
        )

    @classmethod
    async def upadate_title(
        cls, url_code: str, title: str
    ) -> int:
        return await cls.filter(
            url_code=url_code
        ).update(title=title)

    @classmethod
    async def upadate_location(
        cls, url_code: str, location: str
    ) -> int:
        return await cls.filter(
            url_code=url_code
        ).update(location=location)
