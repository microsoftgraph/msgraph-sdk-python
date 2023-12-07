from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration


@dataclass
class CertificateBasedAuthConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[CertificateBasedAuthConfiguration]
):
    value: Optional[List[CertificateBasedAuthConfiguration]] = None

    def __init__(self):
        super().__init__(entity=CertificateBasedAuthConfiguration)
