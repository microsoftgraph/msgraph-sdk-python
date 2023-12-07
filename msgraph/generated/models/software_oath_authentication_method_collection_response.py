from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod


@dataclass
class SoftwareOathAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[SoftwareOathAuthenticationMethod]
):
    value: Optional[List[SoftwareOathAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=SoftwareOathAuthenticationMethod)
