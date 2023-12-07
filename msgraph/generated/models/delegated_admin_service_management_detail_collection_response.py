from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail


@dataclass
class DelegatedAdminServiceManagementDetailCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedAdminServiceManagementDetail]
):
    value: Optional[List[DelegatedAdminServiceManagementDetail]] = None

    def __init__(self):
        super().__init__(entity=DelegatedAdminServiceManagementDetail)
