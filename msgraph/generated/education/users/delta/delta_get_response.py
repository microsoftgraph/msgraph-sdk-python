from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_delta_function_response import BaseDeltaFunctionResponse
from ....models.education_user import EducationUser


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[EducationUser]] = None

    def __init__(self):
        super().__init__(entity=EducationUser)
