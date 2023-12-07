from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .agreement import Agreement
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AgreementCollectionResponse(BaseCollectionPaginationCountResponse[Agreement]):
    value: Optional[List[Agreement]] = None

    def __init__(self):
        super().__init__(entity=Agreement)
