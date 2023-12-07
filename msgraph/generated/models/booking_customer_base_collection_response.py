from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_customer_base import BookingCustomerBase


@dataclass
class BookingCustomerBaseCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingCustomerBase]
):
    value: Optional[List[BookingCustomerBase]] = None

    def __init__(self):
        super().__init__(entity=BookingCustomerBase)
