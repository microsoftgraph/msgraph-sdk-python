from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .provisioning_object_summary import ProvisioningObjectSummary


@dataclass
class ProvisioningObjectSummaryCollectionResponse(
    BaseCollectionPaginationCountResponse[ProvisioningObjectSummary]
):
    value: Optional[List[ProvisioningObjectSummary]] = None

    def __init__(self):
        super().__init__(entity=ProvisioningObjectSummary)
