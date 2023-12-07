from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .detected_app import DetectedApp


@dataclass
class DetectedAppCollectionResponse(BaseCollectionPaginationCountResponse[DetectedApp]):
    value: Optional[List[DetectedApp]] = None

    def __init__(self):
        super().__init__(entity=DetectedApp)
