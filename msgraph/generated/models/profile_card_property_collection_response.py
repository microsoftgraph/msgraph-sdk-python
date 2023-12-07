from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .profile_card_property import ProfileCardProperty


@dataclass
class ProfileCardPropertyCollectionResponse(
    BaseCollectionPaginationCountResponse[ProfileCardProperty]
):
    value: Optional[List[ProfileCardProperty]] = None

    def __init__(self):
        super().__init__(entity=ProfileCardProperty)
