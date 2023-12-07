from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .relation import Relation


@dataclass
class RelationCollectionResponse(BaseCollectionPaginationCountResponse[Relation]):
    value: Optional[List[Relation]] = None

    def __init__(self):
        super().__init__(entity=Relation)
