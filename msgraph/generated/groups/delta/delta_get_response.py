from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_delta_function_response import BaseDeltaFunctionResponse
from ...models.group import Group


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[Group]] = None

    def __init__(self):
        super().__init__(entity=Group)
