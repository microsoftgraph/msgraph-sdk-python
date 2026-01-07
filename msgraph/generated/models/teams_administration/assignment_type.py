from enum import Enum

class AssignmentType(str, Enum):
    Direct = "direct",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

