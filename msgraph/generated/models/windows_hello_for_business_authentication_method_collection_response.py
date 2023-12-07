from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .windows_hello_for_business_authentication_method import (
    WindowsHelloForBusinessAuthenticationMethod,
)


@dataclass
class WindowsHelloForBusinessAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[WindowsHelloForBusinessAuthenticationMethod]
):
    value: Optional[List[WindowsHelloForBusinessAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=WindowsHelloForBusinessAuthenticationMethod)
