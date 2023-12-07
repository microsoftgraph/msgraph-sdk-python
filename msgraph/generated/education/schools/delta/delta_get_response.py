from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_delta_function_response import BaseDeltaFunctionResponse
from ....models.education_school import EducationSchool


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[EducationSchool]] = None

    def __init__(self):
        super().__init__(entity=EducationSchool)
