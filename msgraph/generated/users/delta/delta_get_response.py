from __future__ import annotations

from dataclasses import dataclass

from generated.models.base_delta_function_response import BaseDeltaFunctionResponse
from generated.models.user import User


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse[User]):
    def __init__(self):
        super().__init__(entity=User)
