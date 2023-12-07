from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_app_assignment import MobileAppAssignment


@dataclass
class MobileAppAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileAppAssignment]
):
    value: Optional[List[MobileAppAssignment]] = None

    def __init__(self):
        super().__init__(entity=MobileAppAssignment)
