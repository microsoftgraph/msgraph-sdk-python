from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_delta_function_response import BaseDeltaFunctionResponse
from ...models.service_principal import ServicePrincipal


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[ServicePrincipal]] = None

    def __init__(self):
        super().__init__(entity=ServicePrincipal)
