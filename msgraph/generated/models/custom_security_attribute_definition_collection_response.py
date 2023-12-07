from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition


@dataclass
class CustomSecurityAttributeDefinitionCollectionResponse(
    BaseCollectionPaginationCountResponse[CustomSecurityAttributeDefinition]
):
    value: Optional[List[CustomSecurityAttributeDefinition]] = None

    def __init__(self):
        super().__init__(entity=CustomSecurityAttributeDefinition)
