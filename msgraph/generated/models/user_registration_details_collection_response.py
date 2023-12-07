from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_registration_details import UserRegistrationDetails


@dataclass
class UserRegistrationDetailsCollectionResponse(
    BaseCollectionPaginationCountResponse[UserRegistrationDetails]
):
    value: Optional[List[UserRegistrationDetails]] = None

    def __init__(self):
        super().__init__(entity=UserRegistrationDetails)
