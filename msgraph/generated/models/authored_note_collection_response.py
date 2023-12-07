from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authored_note import AuthoredNote
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthoredNoteCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthoredNote]
):
    value: Optional[List[AuthoredNote]] = None

    def __init__(self):
        super().__init__(entity=AuthoredNote)
