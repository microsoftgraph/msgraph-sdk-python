from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .call_transcript import CallTranscript


@dataclass
class CallTranscriptCollectionResponse(
    BaseCollectionPaginationCountResponse[CallTranscript]
):
    value: Optional[List[CallTranscript]] = None

    def __init__(self):
        super().__init__(entity=CallTranscript)
