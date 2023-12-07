from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ediscovery_custodian import EdiscoveryCustodian


@dataclass
class EdiscoveryCustodianCollectionResponse(
    BaseCollectionPaginationCountResponse[EdiscoveryCustodian]
):
    value: Optional[List[EdiscoveryCustodian]] = None

    def __init__(self):
        super().__init__(entity=EdiscoveryCustodian)
