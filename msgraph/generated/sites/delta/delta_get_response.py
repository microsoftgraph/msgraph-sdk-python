from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_delta_function_response import BaseDeltaFunctionResponse
from ...models.site import Site


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[Site]] = None

    def __init__(self):
        super().__init__(entity=Site)
