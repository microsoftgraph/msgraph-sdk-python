from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .service_provisioning_error import ServiceProvisioningError


@dataclass
class ServiceProvisioningErrorCollectionResponse(
    BaseCollectionPaginationCountResponse[ServiceProvisioningError]
):
    value: Optional[List[ServiceProvisioningError]] = None

    def __init__(self):
        super().__init__(entity=ServiceProvisioningError)
