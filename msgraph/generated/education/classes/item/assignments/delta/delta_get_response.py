from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.base_delta_function_response import BaseDeltaFunctionResponse
from ......models.education_assignment import EducationAssignment


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[EducationAssignment]] = None

    def __init__(self):
        super().__init__(entity=EducationAssignment)
