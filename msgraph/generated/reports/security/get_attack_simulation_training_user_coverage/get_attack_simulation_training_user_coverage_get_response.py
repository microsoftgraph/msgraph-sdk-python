from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.attack_simulation_training_user_coverage import AttackSimulationTrainingUserCoverage
from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class GetAttackSimulationTrainingUserCoverageGetResponse(
    BaseCollectionPaginationCountResponse[AttackSimulationTrainingUserCoverage]
):
    value: Optional[List[AttackSimulationTrainingUserCoverage]] = None

    def __init__(self):
        super().__init__(entity=AttackSimulationTrainingUserCoverage)
