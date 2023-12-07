from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .attendance_record import AttendanceRecord
from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse


@dataclass
class AttendanceRecordCollectionResponse(
    BaseCollectionPaginationCountResponse[AttendanceRecord]
):
    value: Optional[List[AttendanceRecord]] = None

    def __init__(self):
        super().__init__(entity=AttendanceRecord)
