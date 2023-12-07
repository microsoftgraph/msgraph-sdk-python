from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .open_shift import OpenShift


@dataclass
class OpenShiftCollectionResponse(BaseCollectionPaginationCountResponse[OpenShift]):
    value: Optional[List[OpenShift]] = None

    def __init__(self):
        super().__init__(entity=OpenShift)
