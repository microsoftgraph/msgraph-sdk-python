from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attribute_set import AttributeSet
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttributeSetCollectionResponse(
    BaseCollectionPaginationCountResponse[AttributeSet]
):
    value: Optional[List[AttributeSet]] = None

    def __init__(self):
        super().__init__(entity=AttributeSet)
