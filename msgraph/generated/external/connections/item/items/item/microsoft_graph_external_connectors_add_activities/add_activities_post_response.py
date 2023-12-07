from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .......models.external_connectors.external_activity_result import ExternalActivityResult


@dataclass
class AddActivitiesPostResponse(
    BaseCollectionPaginationCountResponse[ExternalActivityResult]
):
    value: Optional[List[ExternalActivityResult]] = None

    def __init__(self):
        super().__init__(entity=ExternalActivityResult)
