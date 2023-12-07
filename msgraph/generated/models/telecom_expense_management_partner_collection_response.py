from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .telecom_expense_management_partner import TelecomExpenseManagementPartner


@dataclass
class TelecomExpenseManagementPartnerCollectionResponse(
    BaseCollectionPaginationCountResponse[TelecomExpenseManagementPartner]
):
    value: Optional[List[TelecomExpenseManagementPartner]] = None

    def __init__(self):
        super().__init__(entity=TelecomExpenseManagementPartner)
