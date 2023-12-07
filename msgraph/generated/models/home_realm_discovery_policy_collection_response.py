from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy


@dataclass
class HomeRealmDiscoveryPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[HomeRealmDiscoveryPolicy]
):
    value: Optional[List[HomeRealmDiscoveryPolicy]] = None

    def __init__(self):
        super().__init__(entity=HomeRealmDiscoveryPolicy)
