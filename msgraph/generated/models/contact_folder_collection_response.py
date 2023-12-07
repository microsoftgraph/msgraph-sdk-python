from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .contact_folder import ContactFolder


@dataclass
class ContactFolderCollectionResponse(
    BaseCollectionPaginationCountResponse[ContactFolder]
):
    value: Optional[List[ContactFolder]] = None

    def __init__(self):
        super().__init__(entity=ContactFolder)
