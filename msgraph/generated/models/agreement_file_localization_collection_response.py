from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .agreement_file_localization import AgreementFileLocalization
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AgreementFileLocalizationCollectionResponse(
    BaseCollectionPaginationCountResponse[AgreementFileLocalization]
):
    value: Optional[List[AgreementFileLocalization]] = None

    def __init__(self):
        super().__init__(entity=AgreementFileLocalization)
