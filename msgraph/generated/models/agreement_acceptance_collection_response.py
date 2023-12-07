from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .agreement_acceptance import AgreementAcceptance
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AgreementAcceptanceCollectionResponse(
    BaseCollectionPaginationCountResponse[AgreementAcceptance]
):
    value: Optional[List[AgreementAcceptance]] = None

    def __init__(self):
        super().__init__(entity=AgreementAcceptance)
