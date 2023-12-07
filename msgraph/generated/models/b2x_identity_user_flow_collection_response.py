from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .b2x_identity_user_flow import B2xIdentityUserFlow
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class B2xIdentityUserFlowCollectionResponse(
    BaseCollectionPaginationCountResponse[B2xIdentityUserFlow]
):
    value: Optional[List[B2xIdentityUserFlow]] = None

    def __init__(self):
        super().__init__(entity=B2xIdentityUserFlow)
