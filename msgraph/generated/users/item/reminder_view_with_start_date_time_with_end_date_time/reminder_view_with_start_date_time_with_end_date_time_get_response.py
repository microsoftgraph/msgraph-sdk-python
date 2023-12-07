from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.reminder import Reminder


@dataclass
class ReminderViewWithStartDateTimeWithEndDateTimeGetResponse(
    BaseCollectionPaginationCountResponse[Reminder]
):
    value: Optional[List[Reminder]] = None

    def __init__(self):
        super().__init__(entity=Reminder)
