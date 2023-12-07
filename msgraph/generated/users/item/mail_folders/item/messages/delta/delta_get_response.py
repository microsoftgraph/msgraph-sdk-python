from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .......models.base_delta_function_response import BaseDeltaFunctionResponse
from .......models.message import Message


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[Message]] = None

    def __init__(self):
        super().__init__(entity=Message)
