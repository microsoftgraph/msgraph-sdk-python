from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .custom_callout_extension import CustomCalloutExtension


@dataclass
class CustomCalloutExtensionCollectionResponse(
    BaseCollectionPaginationCountResponse[CustomCalloutExtension]
):
    value: Optional[List[CustomCalloutExtension]] = None

    def __init__(self):
        super().__init__(entity=CustomCalloutExtension)
