from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource


@dataclass
class EdiscoveryNoncustodialDataSourceCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryNoncustodialDataSource]
):
    value: Optional[List[EdiscoveryNoncustodialDataSource]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryNoncustodialDataSource)
