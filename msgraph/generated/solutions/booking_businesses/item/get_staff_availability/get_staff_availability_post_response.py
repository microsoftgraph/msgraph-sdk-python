from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.staff_availability_item import StaffAvailabilityItem


@dataclass
class GetStaffAvailabilityPostResponse(
    BaseCollectionPaginationCountResponse[StaffAvailabilityItem]
):
    value: Optional[List[StaffAvailabilityItem]] = None

    def __init__(self):
        super().__init__(entity=StaffAvailabilityItem)
