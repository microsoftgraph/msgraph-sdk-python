from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization


@dataclass
class OnPremisesDirectorySynchronizationCollectionResponse(
    BaseCollectionPaginationCountResponse[OnPremisesDirectorySynchronization]
):
    value: Optional[List[OnPremisesDirectorySynchronization]] = None

    def __init__(self):
        super().__init__(entity=OnPremisesDirectorySynchronization)
