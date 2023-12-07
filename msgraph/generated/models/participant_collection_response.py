from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .participant import Participant


@dataclass
class ParticipantCollectionResponse(BaseCollectionPaginationCountResponse[Participant]):
    value: Optional[List[Participant]] = None

    def __init__(self):
        super().__init__(entity=Participant)
