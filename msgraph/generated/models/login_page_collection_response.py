from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .login_page import LoginPage


@dataclass
class LoginPageCollectionResponse(BaseCollectionPaginationCountResponse[LoginPage]):
    value: Optional[List[LoginPage]] = None

    def __init__(self):
        super().__init__(entity=LoginPage)
