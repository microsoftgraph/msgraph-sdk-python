from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .extension_property import ExtensionProperty


@dataclass
class ExtensionPropertyCollectionResponse(
    BaseCollectionPaginationCountResponse[ExtensionProperty]
):
    value: Optional[List[ExtensionProperty]] = None

    def __init__(self):
        super().__init__(entity=ExtensionProperty)
