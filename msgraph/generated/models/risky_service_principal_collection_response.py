from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .risky_service_principal import RiskyServicePrincipal


@dataclass
class RiskyServicePrincipalCollectionResponse(
    BaseCollectionPaginationCountResponse[RiskyServicePrincipal]
):
    value: Optional[List[RiskyServicePrincipal]] = None

    def __init__(self):
        super().__init__(entity=RiskyServicePrincipal)
