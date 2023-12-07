from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .custom_task_extension import CustomTaskExtension


@dataclass
class CustomTaskExtensionCollectionResponse(
    BaseCollectionPaginationCountResponse[CustomTaskExtension]
):
    value: Optional[List[CustomTaskExtension]] = None

    def __init__(self):
        super().__init__(entity=CustomTaskExtension)
