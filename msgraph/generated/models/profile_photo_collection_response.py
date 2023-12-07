from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .profile_photo import ProfilePhoto


@dataclass
class ProfilePhotoCollectionResponse(
    BaseCollectionPaginationCountResponse[ProfilePhoto]
):
    value: Optional[List[ProfilePhoto]] = None

    def __init__(self):
        super().__init__(entity=ProfilePhoto)
