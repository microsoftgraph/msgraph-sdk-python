from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .swap_shifts_change_request import SwapShiftsChangeRequest


@dataclass
class SwapShiftsChangeRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[SwapShiftsChangeRequest]
):
    value: Optional[List[SwapShiftsChangeRequest]] = None

    def __init__(self):
        super().__init__(entity=SwapShiftsChangeRequest)
