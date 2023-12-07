from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .schema_extension import SchemaExtension


@dataclass
class SchemaExtensionCollectionResponse(
    BaseCollectionPaginationCountResponse[SchemaExtension]
):
    value: Optional[List[SchemaExtension]] = None

    def __init__(self):
        super().__init__(entity=SchemaExtension)
