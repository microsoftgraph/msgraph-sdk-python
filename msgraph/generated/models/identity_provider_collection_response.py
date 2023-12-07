from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity_provider import IdentityProvider


@dataclass
class IdentityProviderCollectionResponse(
    BaseCollectionPaginationCountResponse[IdentityProvider]
):
    value: Optional[List[IdentityProvider]] = None

    def __init__(self):
        super().__init__(entity=IdentityProvider)
