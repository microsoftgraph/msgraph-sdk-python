from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp


@dataclass
class MicrosoftStoreForBusinessAppCollectionResponse(
    BaseCollectionPaginationCountResponse[MicrosoftStoreForBusinessApp]
):
    value: Optional[List[MicrosoftStoreForBusinessApp]] = None

    def __init__(self):
        super().__init__(entity=MicrosoftStoreForBusinessApp)
