from enum import Enum

class AssignmentCategory(str, Enum):
    Primary = "primary",
    Private = "private",
    Alternate = "alternate",
    UnknownFutureValue = "unknownFutureValue",

