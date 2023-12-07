from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ........models.base_delta_function_response import BaseDeltaFunctionResponse
from ........models.todo_task import TodoTask


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[TodoTask]] = None

    def __init__(self):
        super().__init__(entity=TodoTask)
