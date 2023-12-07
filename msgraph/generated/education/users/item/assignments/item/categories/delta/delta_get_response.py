from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ........models.base_delta_function_response import BaseDeltaFunctionResponse
from ........models.education_category import EducationCategory


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[EducationCategory]] = None

    def __init__(self):
        super().__init__(entity=EducationCategory)
