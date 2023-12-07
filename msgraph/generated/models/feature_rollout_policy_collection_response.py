from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .feature_rollout_policy import FeatureRolloutPolicy


@dataclass
class FeatureRolloutPolicyCollectionResponse(
    BaseCollectionPaginationCountResponse[FeatureRolloutPolicy]
):
    value: Optional[List[FeatureRolloutPolicy]] = None

    def __init__(self):
        super().__init__(entity=FeatureRolloutPolicy)
