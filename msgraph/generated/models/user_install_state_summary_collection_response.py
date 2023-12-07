from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_install_state_summary import UserInstallStateSummary


@dataclass
class UserInstallStateSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[UserInstallStateSummary]
):
    value: Optional[List[UserInstallStateSummary]] = None

    def __init__(self):
        super().__init__(entity=UserInstallStateSummary)
