from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .connection_operation import ConnectionOperation


@dataclass
class ConnectionOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[ConnectionOperation]
):
    value: Optional[List[ConnectionOperation]] = None

    def __init__(self):
        super().__init__(entity=ConnectionOperation)
