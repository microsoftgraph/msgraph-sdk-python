from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ........models.attribute_mapping_function_schema import AttributeMappingFunctionSchema
from ........models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)


@dataclass
class FunctionsGetResponse(
    BaseCollectionPaginationCountResponse[AttributeMappingFunctionSchema]
):
    value: Optional[List[AttributeMappingFunctionSchema]] = None

    def __init__(self):
        super().__init__(entity=AttributeMappingFunctionSchema)
