from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .simulation_automation_run import SimulationAutomationRun


@dataclass
class SimulationAutomationRunCollectionResponse(
    BaseCollectionPaginationCountResponse[SimulationAutomationRun]
):
    value: Optional[List[SimulationAutomationRun]] = None

    def __init__(self):
        super().__init__(entity=SimulationAutomationRun)
