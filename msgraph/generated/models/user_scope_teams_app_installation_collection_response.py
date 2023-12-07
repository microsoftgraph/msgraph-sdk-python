from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation


@dataclass
class UserScopeTeamsAppInstallationCollectionResponse(
    BaseCollectionPaginationCountResponse[UserScopeTeamsAppInstallation]
):
    value: Optional[List[UserScopeTeamsAppInstallation]] = None

    def __init__(self):
        super().__init__(entity=UserScopeTeamsAppInstallation)
