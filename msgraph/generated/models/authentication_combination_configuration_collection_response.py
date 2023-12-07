from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_combination_configuration import AuthenticationCombinationConfiguration
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationCombinationConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationCombinationConfiguration]
):
    value: Optional[List[AuthenticationCombinationConfiguration]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationCombinationConfiguration)
