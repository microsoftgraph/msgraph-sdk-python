from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .email_authentication_method import EmailAuthenticationMethod


@dataclass
class EmailAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[EmailAuthenticationMethod]
):
    value: Optional[List[EmailAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=EmailAuthenticationMethod)
