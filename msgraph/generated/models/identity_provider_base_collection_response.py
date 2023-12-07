from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .identity_provider_base import IdentityProviderBase


@dataclass
class IdentityProviderBaseCollectionResponse(
    BaseCollectionPaginationCountResponse[IdentityProviderBase]
):
    value: Optional[List[IdentityProviderBase]] = None

    def __init__(self):
        super().__init__(entity=IdentityProviderBase)
