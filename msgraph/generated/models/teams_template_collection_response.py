from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_template import TeamsTemplate


@dataclass
class TeamsTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[TeamsTemplate]
):
    value: Optional[List[TeamsTemplate]] = None

    def __init__(self):
        super().__init__(entity=TeamsTemplate)
