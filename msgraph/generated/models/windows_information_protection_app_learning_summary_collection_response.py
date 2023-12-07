from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_information_protection_app_learning_summary import (
    WindowsInformationProtectionAppLearningSummary,
)


@dataclass
class WindowsInformationProtectionAppLearningSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[
        WindowsInformationProtectionAppLearningSummary
    ]
):
    value: Optional[List[WindowsInformationProtectionAppLearningSummary]] = None

    def __init__(self):
        super().__init__(entity=WindowsInformationProtectionAppLearningSummary)
