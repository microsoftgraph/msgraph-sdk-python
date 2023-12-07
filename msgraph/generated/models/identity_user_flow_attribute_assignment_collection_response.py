from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment


@dataclass
class IdentityUserFlowAttributeAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[IdentityUserFlowAttributeAssignment]
):
    value: Optional[List[IdentityUserFlowAttributeAssignment]] = None

    def __init__(self):
        super().__init__(entity=IdentityUserFlowAttributeAssignment)
