from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_strength_policy import AuthenticationStrengthPolicy
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationStrengthPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationStrengthPolicy]
):
    value: Optional[List[AuthenticationStrengthPolicy]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationStrengthPolicy)
