from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .directory_role_template import DirectoryRoleTemplate


@dataclass
class DirectoryRoleTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[DirectoryRoleTemplate]
):
    value: Optional[List[DirectoryRoleTemplate]] = None

    def __init__(self):
        super().__init__(entity=DirectoryRoleTemplate)
