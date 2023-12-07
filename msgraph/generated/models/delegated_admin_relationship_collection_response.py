from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_admin_relationship import DelegatedAdminRelationship


@dataclass
class DelegatedAdminRelationshipCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedAdminRelationship]
):
    value: Optional[List[DelegatedAdminRelationship]] = None

    def __init__(self):
        super().__init__(entity=DelegatedAdminRelationship)
