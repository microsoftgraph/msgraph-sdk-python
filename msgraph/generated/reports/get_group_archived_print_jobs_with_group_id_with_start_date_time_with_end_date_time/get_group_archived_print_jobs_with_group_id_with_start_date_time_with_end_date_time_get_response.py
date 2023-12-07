from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.archived_print_job import ArchivedPrintJob
from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeGetResponse(
    BaseCollectionPaginationCountResponse[ArchivedPrintJob]
):
    value: Optional[List[ArchivedPrintJob]] = None

    def __init__(self):
        super().__init__(entity=ArchivedPrintJob)
