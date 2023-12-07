from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.managed_app_diagnostic_status import ManagedAppDiagnosticStatus


@dataclass
class GetManagedAppDiagnosticStatusesGetResponse(
    BaseCollectionPaginationCountResponse[ManagedAppDiagnosticStatus]
):
    value: Optional[List[ManagedAppDiagnosticStatus]] = None

    def __init__(self):
        super().__init__(entity=ManagedAppDiagnosticStatus)
