from __future__ import annotations

from dataclasses import dataclass

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user import User


@dataclass
class UserCollectionResponse(BaseCollectionPaginationCountResponse[User]):
    def __init__(self):
        super().__init__(entity=User)
