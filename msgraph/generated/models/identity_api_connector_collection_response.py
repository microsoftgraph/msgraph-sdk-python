from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity_api_connector import IdentityApiConnector


@dataclass
class IdentityApiConnectorCollectionResponse(
    BaseCollectionPaginationCountResponse[IdentityApiConnector]
):
    value: Optional[List[IdentityApiConnector]] = None

    def __init__(self):
        super().__init__(entity=IdentityApiConnector)
