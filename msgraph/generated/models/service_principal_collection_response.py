from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_principal import ServicePrincipal


@dataclass
class ServicePrincipalCollectionResponse(
    BaseCollectionPaginationCountResponse[ServicePrincipal]
):
    value: Optional[List[ServicePrincipal]] = None

    def __init__(self):
        super().__init__(entity=ServicePrincipal)
