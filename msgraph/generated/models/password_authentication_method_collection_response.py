from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .password_authentication_method import PasswordAuthenticationMethod


@dataclass
class PasswordAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[PasswordAuthenticationMethod]
):
    value: Optional[List[PasswordAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=PasswordAuthenticationMethod)
