from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .offer_shift_request import OfferShiftRequest


@dataclass
class OfferShiftRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[OfferShiftRequest]
):
    value: Optional[List[OfferShiftRequest]] = None

    def __init__(self):
        super().__init__(entity=OfferShiftRequest)
