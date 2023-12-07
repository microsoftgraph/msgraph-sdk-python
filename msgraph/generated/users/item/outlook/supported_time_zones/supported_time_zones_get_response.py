from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.time_zone_information import TimeZoneInformation


@dataclass
class SupportedTimeZonesGetResponse(
    BaseCollectionPaginationCountResponse[TimeZoneInformation]
):
    value: Optional[List[TimeZoneInformation]] = None

    def __init__(self):
        super().__init__(entity=TimeZoneInformation)
