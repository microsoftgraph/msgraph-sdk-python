from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .bitlocker_recovery_key import BitlockerRecoveryKey


@dataclass
class BitlockerRecoveryKeyCollectionResponse(
    BaseCollectionPaginationCountResponse[BitlockerRecoveryKey]
):
    value: Optional[List[BitlockerRecoveryKey]] = None

    def __init__(self):
        super().__init__(entity=BitlockerRecoveryKey)
