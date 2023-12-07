from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_information_protection_network_learning_summary import (
    WindowsInformationProtectionNetworkLearningSummary,
)


@dataclass
class WindowsInformationProtectionNetworkLearningSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[
        WindowsInformationProtectionNetworkLearningSummary
    ]
):
    value: Optional[List[WindowsInformationProtectionNetworkLearningSummary]] = None

    def __init__(self):
        super().__init__(entity=WindowsInformationProtectionNetworkLearningSummary)
