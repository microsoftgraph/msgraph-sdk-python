from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .secure_score_control_profile import SecureScoreControlProfile


@dataclass
class SecureScoreControlProfileCollectionResponse(
    BaseCollectionPaginationCountResponse[SecureScoreControlProfile]
):
    value: Optional[List[SecureScoreControlProfile]] = None

    def __init__(self):
        super().__init__(entity=SecureScoreControlProfile)
