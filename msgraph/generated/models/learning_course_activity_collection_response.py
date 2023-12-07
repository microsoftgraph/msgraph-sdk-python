from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .learning_course_activity import LearningCourseActivity


@dataclass
class LearningCourseActivityCollectionResponse(
    BaseCollectionPaginationCountResponse[LearningCourseActivity]
):
    value: Optional[List[LearningCourseActivity]] = None

    def __init__(self):
        super().__init__(entity=LearningCourseActivity)
