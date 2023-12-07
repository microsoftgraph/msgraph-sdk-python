from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .open_shift_change_request import OpenShiftChangeRequest


@dataclass
class OpenShiftChangeRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[OpenShiftChangeRequest]
):
    value: Optional[List[OpenShiftChangeRequest]] = None

    def __init__(self):
        super().__init__(entity=OpenShiftChangeRequest)
