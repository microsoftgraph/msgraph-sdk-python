from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.attack_simulation_repeat_offender import AttackSimulationRepeatOffender
from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetAttackSimulationRepeatOffendersGetResponse(
    BaseCollectionPaginationCountResponse[AttackSimulationRepeatOffender]
):
    value: Optional[List[AttackSimulationRepeatOffender]] = None

    def __init__(self):
        super().__init__(entity=AttackSimulationRepeatOffender)
