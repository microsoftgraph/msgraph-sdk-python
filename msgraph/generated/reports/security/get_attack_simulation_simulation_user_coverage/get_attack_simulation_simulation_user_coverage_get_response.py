from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.attack_simulation_simulation_user_coverage import (
    AttackSimulationSimulationUserCoverage,
)
from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetAttackSimulationSimulationUserCoverageGetResponse(
    BaseCollectionPaginationCountResponse[AttackSimulationSimulationUserCoverage]
):
    value: Optional[List[AttackSimulationSimulationUserCoverage]] = None

    def __init__(self):
        super().__init__(entity=AttackSimulationSimulationUserCoverage)
