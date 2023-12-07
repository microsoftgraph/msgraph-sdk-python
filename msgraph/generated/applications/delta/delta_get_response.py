from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.application import Application
from ...models.base_delta_function_response import BaseDeltaFunctionResponse


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[Application]] = None

    def __init__(self):
        super().__init__(entity=Application)
