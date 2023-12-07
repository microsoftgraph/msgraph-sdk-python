from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .agreement_file_version import AgreementFileVersion
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AgreementFileVersionCollectionResponse(
    BaseCollectionPaginationCountResponse[AgreementFileVersion]
):
    value: Optional[List[AgreementFileVersion]] = None

    def __init__(self):
        super().__init__(entity=AgreementFileVersion)
