from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .data_policy_operation import DataPolicyOperation


@dataclass
class DataPolicyOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[DataPolicyOperation]
):
    value: Optional[List[DataPolicyOperation]] = None

    def __init__(self):
        super().__init__(entity=DataPolicyOperation)
