from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .phone_authentication_method import PhoneAuthenticationMethod


@dataclass
class PhoneAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[PhoneAuthenticationMethod]
):
    value: Optional[List[PhoneAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=PhoneAuthenticationMethod)
