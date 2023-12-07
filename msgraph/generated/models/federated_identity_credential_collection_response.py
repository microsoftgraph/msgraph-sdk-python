from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .federated_identity_credential import FederatedIdentityCredential


@dataclass
class FederatedIdentityCredentialCollectionResponse(
    BaseCollectionPaginationCountResponse[FederatedIdentityCredential]
):
    value: Optional[List[FederatedIdentityCredential]] = None

    def __init__(self):
        super().__init__(entity=FederatedIdentityCredential)
