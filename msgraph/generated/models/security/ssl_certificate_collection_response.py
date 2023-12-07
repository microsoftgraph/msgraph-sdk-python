from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .ssl_certificate import SslCertificate


@dataclass
class SslCertificateCollectionResponse(
    BaseCollectionPaginationCountResponse[SslCertificate]
):
    value: Optional[List[SslCertificate]] = None

    def __init__(self):
        super().__init__(entity=SslCertificate)
