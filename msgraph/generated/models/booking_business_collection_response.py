from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_business import BookingBusiness


@dataclass
class BookingBusinessCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingBusiness]
):
    value: Optional[List[BookingBusiness]] = None

    def __init__(self):
        super().__init__(entity=BookingBusiness)
