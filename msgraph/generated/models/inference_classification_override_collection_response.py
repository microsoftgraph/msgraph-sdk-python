from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .inference_classification_override import InferenceClassificationOverride


@dataclass
class InferenceClassificationOverrideCollectionResponse(
    BaseCollectionPaginationCountResponse[InferenceClassificationOverride]
):
    value: Optional[List[InferenceClassificationOverride]] = None

    def __init__(self):
        super().__init__(entity=InferenceClassificationOverride)
