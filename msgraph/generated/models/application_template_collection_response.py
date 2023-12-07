from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .application_template import ApplicationTemplate
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class ApplicationTemplateCollectionResponse(
    BaseCollectionPaginationCountResponse[ApplicationTemplate]
):
    value: Optional[List[ApplicationTemplate]] = None

    def __init__(self):
        super().__init__(entity=ApplicationTemplate)
