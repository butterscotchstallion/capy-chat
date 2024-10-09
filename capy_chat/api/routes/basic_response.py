from dataclasses import dataclass
from typing import Literal

from typing_extensions import TypedDict


@dataclass
class BasicResponse(TypedDict):
    status: Literal["OK"] | Literal["ERROR"]
    details: dict
