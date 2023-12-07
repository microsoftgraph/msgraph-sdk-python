from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .meeting_attendance_report import MeetingAttendanceReport


@dataclass
class MeetingAttendanceReportCollectionResponse(
    BaseCollectionPaginationCountResponse[MeetingAttendanceReport]
):
    value: Optional[List[MeetingAttendanceReport]] = None

    def __init__(self):
        super().__init__(entity=MeetingAttendanceReport)
