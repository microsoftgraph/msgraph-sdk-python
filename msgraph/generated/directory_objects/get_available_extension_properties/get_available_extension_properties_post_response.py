from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ...models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ...models.extension_property import ExtensionProperty


@dataclass
class GetAvailableExtensionPropertiesPostResponse(
    BaseCollectionPaginationCountResponse[ExtensionProperty]
):
    value: Optional[List[ExtensionProperty]] = None

    def __init__(self):
        super().__init__(entity=ExtensionProperty)
