from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .incident import Incident


@dataclass
class IncidentCollectionResponse(BaseCollectionPaginationCountResponse[Incident]):
    value: Optional[List[Incident]] = None

    def __init__(self):
        super().__init__(entity=Incident)
