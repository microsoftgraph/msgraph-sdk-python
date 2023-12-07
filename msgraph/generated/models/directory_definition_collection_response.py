from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .directory_definition import DirectoryDefinition


@dataclass
class DirectoryDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[DirectoryDefinition]
):
    value: Optional[List[DirectoryDefinition]] = None

    def __init__(self):
        super().__init__(entity=DirectoryDefinition)
