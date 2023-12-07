from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .print_connector import PrintConnector


@dataclass
class PrintConnectorCollectionResponse(
    BaseCollectionPaginationCountResponse[PrintConnector]
):
    value: Optional[List[PrintConnector]] = None

    def __init__(self):
        super().__init__(entity=PrintConnector)
