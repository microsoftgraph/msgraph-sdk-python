from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_delta_function_response import BaseDeltaFunctionResponse
from ...models.org_contact import OrgContact


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[OrgContact]] = None

    def __init__(self):
        super().__init__(entity=OrgContact)
