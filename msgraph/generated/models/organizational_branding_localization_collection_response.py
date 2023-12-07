from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .organizational_branding_localization import OrganizationalBrandingLocalization


@dataclass
class OrganizationalBrandingLocalizationCollectionResponse(
    BaseCollectionPaginationCountResponse[OrganizationalBrandingLocalization]
):
    value: Optional[List[OrganizationalBrandingLocalization]] = None

    def __init__(self):
        super().__init__(entity=OrganizationalBrandingLocalization)
