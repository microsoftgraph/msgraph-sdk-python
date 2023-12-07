from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .conditional_access_template import ConditionalAccessTemplate


@dataclass
class ConditionalAccessTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[ConditionalAccessTemplate]
):
    value: Optional[List[ConditionalAccessTemplate]] = None

    def __init__(self):
        super().__init__(entity=ConditionalAccessTemplate)
