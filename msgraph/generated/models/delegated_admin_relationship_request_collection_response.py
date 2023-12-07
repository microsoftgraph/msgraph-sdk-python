from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest


@dataclass
class DelegatedAdminRelationshipRequestCollectionResponse(
    BaseCollectionPaginationCountResponse[DelegatedAdminRelationshipRequest]
):
    value: Optional[List[DelegatedAdminRelationshipRequest]] = None

    def __init__(self):
        super().__init__(entity=DelegatedAdminRelationshipRequest)
