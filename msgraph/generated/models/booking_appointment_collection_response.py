from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .booking_appointment import BookingAppointment


@dataclass
class BookingAppointmentCollectionResponse(
    BaseCollectionPaginationCountResponse[BookingAppointment]
):
    value: Optional[List[BookingAppointment]] = None

    def __init__(self):
        super().__init__(entity=BookingAppointment)
