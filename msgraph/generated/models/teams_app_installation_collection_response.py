from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .teams_app_installation import TeamsAppInstallation


@dataclass
class TeamsAppInstallationCollectionResponse(
    BaseCollectionPaginationCountResponse[TeamsAppInstallation]
):
    value: Optional[List[TeamsAppInstallation]] = None

    def __init__(self):
        super().__init__(entity=TeamsAppInstallation)
