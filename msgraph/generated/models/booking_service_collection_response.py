from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_service import BookingService


@dataclass
class BookingServiceCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingService]
):
    value: Optional[List[BookingService]] = None

    def __init__(self):
        super().__init__(entity=BookingService)
