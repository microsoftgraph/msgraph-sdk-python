from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .authentication_context_class_reference import AuthenticationContextClassReference
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AuthenticationContextClassReferenceCollectionResponse(
    BaseCollectionPaginationCountResponse[AuthenticationContextClassReference]
):
    value: Optional[List[AuthenticationContextClassReference]] = None

    def __init__(self):
        super().__init__(entity=AuthenticationContextClassReference)
