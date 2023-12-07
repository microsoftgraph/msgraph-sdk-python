from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .device_local_credential_info import DeviceLocalCredentialInfo


@dataclass
class DeviceLocalCredentialInfoCollectionResponse(
    BaseCollectionPaginationCountResponse[DeviceLocalCredentialInfo]
):
    value: Optional[List[DeviceLocalCredentialInfo]] = None

    def __init__(self):
        super().__init__(entity=DeviceLocalCredentialInfo)
