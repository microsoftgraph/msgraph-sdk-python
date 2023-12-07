from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_information_protection_policy import WindowsInformationProtectionPolicy


@dataclass
class WindowsInformationProtectionPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsInformationProtectionPolicy]
):
    value: Optional[List[WindowsInformationProtectionPolicy]] = None

    def __init__(self):
        super().__init__(entity=WindowsInformationProtectionPolicy)
