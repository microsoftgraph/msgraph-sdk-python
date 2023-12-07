from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ........models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ........models.schedule_information import ScheduleInformation


@dataclass
class GetSchedulePostResponse(
    BaseCollectionPaginationCountResponse[ScheduleInformation]
):
    value: Optional[List[ScheduleInformation]] = None

    def __init__(self):
        super().__init__(entity=ScheduleInformation)
