from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .host_ssl_certificate import HostSslCertificate


@dataclass
class HostSslCertificateCollectionResponse(
    BaseCollectionPaginationCountResponse[HostSslCertificate]
):
    value: Optional[List[HostSslCertificate]] = None

    def __init__(self):
        super().__init__(entity=HostSslCertificate)
