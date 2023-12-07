from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_method import AuthenticationMethod
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationMethod]
):
    value: Optional[List[AuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationMethod)
