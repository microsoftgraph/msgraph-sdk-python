from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .o_auth2_permission_grant import OAuth2PermissionGrant


@dataclass
class OAuth2PermissionGrantCollectionResponse(
    BaseCollectionPaginationCountResponse[OAuth2PermissionGrant]
):
    value: Optional[List[OAuth2PermissionGrant]] = None

    def __init__(self):
        super().__init__(entity=OAuth2PermissionGrant)
