from __future__ import annotations

import dataclasses
import uuid
from datetime import date
from typing import Iterable

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG
from app.tortoise_models.meeting import (
    MeetingModel,
)
from app.tortoise_models.participant_date import (
    ParticipantDateModel,
)


class ParticipantDateResponse(BaseModel):
    model_config = FROZEN_CONFIG
    date: date
    enabled: bool
    starred: bool
    id: uuid.UUID | int


class ParticipantResponse(BaseModel):
    model_config = FROZEN_CONFIG
    id: uuid.UUID | int
    name: str
    dates: list[ParticipantDateResponse]


@dataclasses.dataclass
class BestDate:
    date: date
    enable_count: int
    star_count: int


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG
    url_code: str
    start_date: date | None = None
    end_date: date | None = None
    title: str
    location: str
    participants: list[ParticipantResponse]
    best_dates: list[date]

    @classmethod
    def from_mysql(
        cls, meeting: MeetingModel
    ) -> GetMeetingResponse:
        return GetMeetingResponse(
            url_code=meeting.url_code,
            end_date=meeting.end_date,
            start_date=meeting.start_date,
            title=meeting.title,
            location="test",
            participants=[
                ParticipantResponse(
                    id=p.id,
                    name=p.name,
                    dates=[
                        ParticipantDateResponse(
                            date=pd.date,
                            id=pd.id,
                            enabled=pd.enabled,
                            starred=pd.starred,
                        )
                        for pd in p.participant_dates
                    ],
                )
                for p in meeting.participants
            ],
            best_dates=cls._get_best_dates(
                (
                    participant_date
                    for participant in meeting.participants
                    for participant_date in participant.participant_dates
                )
            ),
        )

    @classmethod
    def _get_best_dates(
        cls,
        participant_dates: Iterable[
            ParticipantDateModel
        ],
    ) -> list[date]:
        result_dict: dict[date, BestDate] = {}

        for participant_date in participant_dates:
            # 여기에 print 문 추가
            print(
                f"DEBUG: Date: {participant_date.date}, Enabled: {participant_date.enabled}, Starred: {participant_date.starred}"
            )

            if (
                participant_date.date
                not in result_dict
            ):
                result_dict[
                    participant_date.date  # Key 값
                ] = BestDate(
                    date=participant_date.date,  # Value 값
                    enable_count=0,
                    star_count=0,
                )
                if participant_date.enabled:
                    result_dict[
                        participant_date.date
                    ].enable_count += 1
                if participant_date.starred:
                    result_dict[
                        participant_date.date
                    ].star_count += 1

        result_list = list(result_dict.values())
        result_list.sort(
            key=lambda best_date: (
                -best_date.enable_count,
                -best_date.star_count,
                best_date.date,
            ),
        )
        return [
            best_date.date
            for best_date in result_list[:3]
        ]
