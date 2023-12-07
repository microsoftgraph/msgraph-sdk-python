from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .directory_object import DirectoryObject


@dataclass
class DirectoryObjectCollectionResponse(
    BaseCollectionPaginationCountResponse[DirectoryObject]
):
    value: Optional[List[DirectoryObject]] = None

    def __init__(self):
        super().__init__(entity=DirectoryObject)
