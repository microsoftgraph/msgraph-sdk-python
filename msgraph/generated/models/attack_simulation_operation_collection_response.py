from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attack_simulation_operation import AttackSimulationOperation
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttackSimulationOperationCollectionResponse(
    BaseCollectionPaginationCountResponse[AttackSimulationOperation]
):
    value: Optional[List[AttackSimulationOperation]] = None

    def __init__(self):
        super().__init__(entity=AttackSimulationOperation)
