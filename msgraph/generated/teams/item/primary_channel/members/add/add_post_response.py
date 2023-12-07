from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ......models.action_result_part import ActionResultPart
from ......models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class AddPostResponse(BaseCollectionPaginationCountResponse[ActionResultPart]):
    value: Optional[List[ActionResultPart]] = None

    def __init__(self):
        super().__init__(entity=ActionResultPart)
