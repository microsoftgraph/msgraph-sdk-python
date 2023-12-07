from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .compliance_management_partner import ComplianceManagementPartner


@dataclass
class ComplianceManagementPartnerCollectionResponse(
    BaseCollectionPaginationCountResponse[ComplianceManagementPartner]
):
    value: Optional[List[ComplianceManagementPartner]] = None

    def __init__(self):
        super().__init__(entity=ComplianceManagementPartner)
