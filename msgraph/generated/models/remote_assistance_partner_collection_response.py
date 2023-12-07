from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .remote_assistance_partner import RemoteAssistancePartner


@dataclass
class RemoteAssistancePartnerCollectionResponse(
    BaseCollectionPaginationCountResponse[RemoteAssistancePartner]
):
    value: Optional[List[RemoteAssistancePartner]] = None

    def __init__(self):
        super().__init__(entity=RemoteAssistancePartner)
