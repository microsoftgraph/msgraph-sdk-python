from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .invitation import Invitation


@dataclass
class InvitationCollectionResponse(BaseCollectionPaginationCountResponse[Invitation]):
    value: Optional[List[Invitation]] = None

    def __init__(self):
        super().__init__(entity=Invitation)
