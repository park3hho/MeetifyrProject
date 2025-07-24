from typing import Annotated

from pydantic import BaseModel, Field

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):  # new*
    model_config = FROZEN_CONFIG

    url_code: Annotated[
        str,
        Field(
            description="m미팅 유앙ㄹㅇㄹ유닉!"
        ),
    ]
