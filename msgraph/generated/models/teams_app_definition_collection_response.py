from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_app_definition import TeamsAppDefinition


@dataclass
class TeamsAppDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[TeamsAppDefinition]
):
    value: Optional[List[TeamsAppDefinition]] = None

    def __init__(self):
        super().__init__(entity=TeamsAppDefinition)
