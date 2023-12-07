from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .cross_tenant_access_policy_configuration_partner import (
    CrossTenantAccessPolicyConfigurationPartner,
)


@dataclass
class CrossTenantAccessPolicyConfigurationPartnerCollectionResponse(
    BaseCollectionPaginationCountResponse[CrossTenantAccessPolicyConfigurationPartner]
):
    value: Optional[List[CrossTenantAccessPolicyConfigurationPartner]] = None

    def __init__(self):
        super().__init__(entity=CrossTenantAccessPolicyConfigurationPartner)
