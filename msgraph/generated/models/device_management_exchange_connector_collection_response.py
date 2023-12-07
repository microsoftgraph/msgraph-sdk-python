from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_management_exchange_connector import DeviceManagementExchangeConnector


@dataclass
class DeviceManagementExchangeConnectorCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceManagementExchangeConnector]
):
    value: Optional[List[DeviceManagementExchangeConnector]] = None

    def __init__(self):
        super().__init__(entity=DeviceManagementExchangeConnector)
