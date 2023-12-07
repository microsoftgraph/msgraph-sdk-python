from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .connected_organization import ConnectedOrganization


@dataclass
class ConnectedOrganizationCollectionResponse(
    BaseCollectionPaginationCountResponse[ConnectedOrganization]
):
    value: Optional[List[ConnectedOrganization]] = None

    def __init__(self):
        super().__init__(entity=ConnectedOrganization)
