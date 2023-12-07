from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .access_package_question import AccessPackageQuestion
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AccessPackageQuestionCollectionResponse(
    BaseCollectionPaginationCountResponse[AccessPackageQuestion]
):
    value: Optional[List[AccessPackageQuestion]] = None

    def __init__(self):
        super().__init__(entity=AccessPackageQuestion)
