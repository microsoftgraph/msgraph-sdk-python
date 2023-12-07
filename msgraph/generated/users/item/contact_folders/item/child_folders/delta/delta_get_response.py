from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .......models.base_delta_function_response import BaseDeltaFunctionResponse
from .......models.contact_folder import ContactFolder


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[ContactFolder]] = None

    def __init__(self):
        super().__init__(entity=ContactFolder)
