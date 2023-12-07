from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity_user_flow_attribute import IdentityUserFlowAttribute


@dataclass
class IdentityUserFlowAttributeCollectionResponse(
    BaseCollectionPaginationCountResponse[IdentityUserFlowAttribute]
):
    value: Optional[List[IdentityUserFlowAttribute]] = None

    def __init__(self):
        super().__init__(entity=IdentityUserFlowAttribute)
