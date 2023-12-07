from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.call_records.pstn_call_log_row import PstnCallLogRow


@dataclass
class GetPstnCallsWithFromDateTimeWithToDateTimeGetResponse(
    BaseCollectionPaginationCountResponse[PstnCallLogRow]
):
    value: Optional[List[PstnCallLogRow]] = None

    def __init__(self):
        super().__init__(entity=PstnCallLogRow)
