from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .simulation_automation import SimulationAutomation


@dataclass
class SimulationAutomationCollectionResponse(
    BaseCollectionPaginationCountResponse[SimulationAutomation]
):
    value: Optional[List[SimulationAutomation]] = None

    def __init__(self):
        super().__init__(entity=SimulationAutomation)
