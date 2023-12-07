from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .user_flow_language_configuration import UserFlowLanguageConfiguration


@dataclass
class UserFlowLanguageConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[UserFlowLanguageConfiguration]
):
    value: Optional[List[UserFlowLanguageConfiguration]] = None

    def __init__(self):
        super().__init__(entity=UserFlowLanguageConfiguration)
