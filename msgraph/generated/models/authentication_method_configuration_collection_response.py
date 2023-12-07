from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_method_configuration import AuthenticationMethodConfiguration
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationMethodConfigurationCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationMethodConfiguration]
):
    value: Optional[List[AuthenticationMethodConfiguration]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationMethodConfiguration)
