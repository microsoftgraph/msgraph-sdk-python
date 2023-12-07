from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_custom_question import BookingCustomQuestion


@dataclass
class BookingCustomQuestionCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingCustomQuestion]
):
    value: Optional[List[BookingCustomQuestion]] = None

    def __init__(self):
        super().__init__(entity=BookingCustomQuestion)
