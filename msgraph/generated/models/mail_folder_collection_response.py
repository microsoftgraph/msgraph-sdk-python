from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .mail_folder import MailFolder


@dataclass
class MailFolderCollectionResponse(BaseCollectionPaginationCountResponse[MailFolder]):
    value: Optional[List[MailFolder]] = None

    def __init__(self):
        super().__init__(entity=MailFolder)
