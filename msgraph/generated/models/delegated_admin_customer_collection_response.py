from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_admin_customer import DelegatedAdminCustomer


@dataclass
class DelegatedAdminCustomerCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedAdminCustomer]
):
    value: Optional[List[DelegatedAdminCustomer]] = None

    def __init__(self):
        super().__init__(entity=DelegatedAdminCustomer)
