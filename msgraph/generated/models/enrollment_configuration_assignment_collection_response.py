from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment


@dataclass
class EnrollmentConfigurationAssignmentCollectionResponse(
    BaseCollectionPaginationCountResponse[EnrollmentConfigurationAssignment]
):
    value: Optional[List[EnrollmentConfigurationAssignment]] = None

    def __init__(self):
        super().__init__(entity=EnrollmentConfigurationAssignment)
