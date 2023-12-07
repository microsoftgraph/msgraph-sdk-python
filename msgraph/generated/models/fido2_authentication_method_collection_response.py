from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .fido2_authentication_method import Fido2AuthenticationMethod


@dataclass
class Fido2AuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[Fido2AuthenticationMethod]
):
    value: Optional[List[Fido2AuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=Fido2AuthenticationMethod)
