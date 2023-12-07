from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .onenote_operation import OnenoteOperation


@dataclass
class OnenoteOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[OnenoteOperation]
):
    value: Optional[List[OnenoteOperation]] = None

    def __init__(self):
        super().__init__(entity=OnenoteOperation)
