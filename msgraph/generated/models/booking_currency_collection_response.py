from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_currency import BookingCurrency


@dataclass
class BookingCurrencyCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingCurrency]
):
    value: Optional[List[BookingCurrency]] = None

    def __init__(self):
        super().__init__(entity=BookingCurrency)
