from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.content_type import ContentType


@dataclass
class GetApplicableContentTypesForListWithListIdGetResponse(
    BaseCollectionPaginationCountResponse[ContentType]
):
    value: Optional[List[ContentType]] = None

    def __init__(self):
        super().__init__(entity=ContentType)
