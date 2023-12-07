from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .data_source import DataSource


@dataclass
class DataSourceCollectionResponse(BaseCollectionPaginationCountResponse[DataSource]):
    value: Optional[List[DataSource]] = None

    def __init__(self):
        super().__init__(entity=DataSource)
