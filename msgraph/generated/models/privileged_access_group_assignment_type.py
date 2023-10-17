from enum import Enum

class PrivilegedAccessGroupAssignmentType(str, Enum):
    Assigned = "assigned",
    Activated = "activated",
    UnknownFutureValue = "unknownFutureValue",

