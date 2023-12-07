from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .column_definition import ColumnDefinition


@dataclass
class ColumnDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[ColumnDefinition]
):
    value: Optional[List[ColumnDefinition]] = None

    def __init__(self):
        super().__init__(entity=ColumnDefinition)
