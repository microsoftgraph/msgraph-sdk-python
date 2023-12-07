from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mobile_threat_defense_connector import MobileThreatDefenseConnector


@dataclass
class MobileThreatDefenseConnectorCollectionResponse(
    BaseCollectionPaginationCountResponse[MobileThreatDefenseConnector]
):
    value: Optional[List[MobileThreatDefenseConnector]] = None

    def __init__(self):
        super().__init__(entity=MobileThreatDefenseConnector)
