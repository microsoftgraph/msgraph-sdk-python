from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.convert_id_result import ConvertIdResult


@dataclass
class TranslateExchangeIdsPostResponse(
    BaseCollectionPaginationCountResponse[ConvertIdResult]
):
    value: Optional[List[ConvertIdResult]] = None

    def __init__(self):
        super().__init__(entity=ConvertIdResult)
