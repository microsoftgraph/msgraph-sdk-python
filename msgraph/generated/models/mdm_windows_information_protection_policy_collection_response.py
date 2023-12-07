from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy


@dataclass
class MdmWindowsInformationProtectionPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[MdmWindowsInformationProtectionPolicy]
):
    value: Optional[List[MdmWindowsInformationProtectionPolicy]] = None

    def __init__(self):
        super().__init__(entity=MdmWindowsInformationProtectionPolicy)
