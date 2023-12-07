from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .administrative_unit import AdministrativeUnit
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AdministrativeUnitCollectionResponse(
    BaseCollectionPaginationCountResponse[AdministrativeUnit]
):
    value: Optional[List[AdministrativeUnit]] = None

    def __init__(self):
        super().__init__(entity=AdministrativeUnit)
