from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_update_message import ServiceUpdateMessage


@dataclass
class ServiceUpdateMessageCollectionResponse(
    BaseCollectionPaginationCountResponse[ServiceUpdateMessage]
):
    value: Optional[List[ServiceUpdateMessage]] = None

    def __init__(self):
        super().__init__(entity=ServiceUpdateMessage)
