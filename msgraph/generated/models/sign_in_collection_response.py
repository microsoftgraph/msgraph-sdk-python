from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .sign_in import SignIn


@dataclass
class SignInCollectionResponse(BaseCollectionPaginationCountResponse[SignIn]):
    value: Optional[List[SignIn]] = None

    def __init__(self):
        super().__init__(entity=SignIn)
