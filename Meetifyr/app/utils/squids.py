import random
from datetime import datetime
from typing import Sequence

from sqids import sqids

squid = sqids.Sqids()


class Squids:
    @classmethod
    def encode(cls, nums: Sequence[int]) -> str:
        return squid.encode(nums)


if __name__ == '__main__':
    now = datetime.now()
    print(
        Squids.encode(
            [
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.second,
                now.microsecond,
                random.randint(1, 9),
            ]
        )
    )
