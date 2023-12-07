from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .directory_role import DirectoryRole


@dataclass
class DirectoryRoleCollectionResponse(
    BaseCollectionPaginationCountResponse[DirectoryRole]
):
    value: Optional[List[DirectoryRole]] = None

    def __init__(self):
        super().__init__(entity=DirectoryRole)
