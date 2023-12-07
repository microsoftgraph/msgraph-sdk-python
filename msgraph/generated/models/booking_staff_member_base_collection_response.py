from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_staff_member_base import BookingStaffMemberBase


@dataclass
class BookingStaffMemberBaseCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingStaffMemberBase]
):
    value: Optional[List[BookingStaffMemberBase]] = None

    def __init__(self):
        super().__init__(entity=BookingStaffMemberBase)
