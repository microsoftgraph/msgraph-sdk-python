from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod


@dataclass
class TemporaryAccessPassAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[TemporaryAccessPassAuthenticationMethod]
):
    value: Optional[List[TemporaryAccessPassAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=TemporaryAccessPassAuthenticationMethod)
