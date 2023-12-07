from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .internal_domain_federation import InternalDomainFederation


@dataclass
class InternalDomainFederationCollectionResponse(
    BaseCollectionPaginationCountResponse[InternalDomainFederation]
):
    value: Optional[List[InternalDomainFederation]] = None

    def __init__(self):
        super().__init__(entity=InternalDomainFederation)
