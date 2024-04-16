from enum import Enum

class EducationAssignmentStatus(str, Enum):
    Draft = "draft",
    Published = "published",
    Assigned = "assigned",
    UnknownFutureValue = "unknownFutureValue",
    Inactive = "inactive",

