from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_delta_function_response import BaseDeltaFunctionResponse
from ...models.o_auth2_permission_grant import OAuth2PermissionGrant


@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    value: Optional[List[OAuth2PermissionGrant]] = None

    def __init__(self):
        super().__init__(entity=OAuth2PermissionGrant)
