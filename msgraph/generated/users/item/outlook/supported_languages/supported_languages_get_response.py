from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from .....models.locale_info import LocaleInfo


@dataclass
class SupportedLanguagesGetResponse(BaseCollectionPaginationCountResponse[LocaleInfo]):
    value: Optional[List[LocaleInfo]] = None

    def __init__(self):
        super().__init__(entity=LocaleInfo)
