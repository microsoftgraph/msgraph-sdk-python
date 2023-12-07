from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_method_mode_detail import AuthenticationMethodModeDetail
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationMethodModeDetailCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationMethodModeDetail]
):
    value: Optional[List[AuthenticationMethodModeDetail]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationMethodModeDetail)
