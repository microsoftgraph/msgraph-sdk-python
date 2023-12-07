from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.call_records.direct_routing_log_row import DirectRoutingLogRow


@dataclass
class GetDirectRoutingCallsWithFromDateTimeWithToDateTimeGetResponse(
    BaseCollectionPaginationCountResponse[DirectRoutingLogRow]
):
    value: Optional[List[DirectRoutingLogRow]] = None

    def __init__(self):
        super().__init__(entity=DirectRoutingLogRow)
