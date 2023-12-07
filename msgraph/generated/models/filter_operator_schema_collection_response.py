from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .filter_operator_schema import FilterOperatorSchema


@dataclass
class FilterOperatorSchemaCollectionResponse(
    BaseCollectionPaginationCountResponse[FilterOperatorSchema]
):
    value: Optional[List[FilterOperatorSchema]] = None

    def __init__(self):
        super().__init__(entity=FilterOperatorSchema)
