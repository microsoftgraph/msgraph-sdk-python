from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttributeMappingFunctionSchemaCollectionResponse(
    BaseCollectionPaginationCountResponse[AttributeMappingFunctionSchema]
):
    value: Optional[List[AttributeMappingFunctionSchema]] = None

    def __init__(self):
        super().__init__(entity=AttributeMappingFunctionSchema)
