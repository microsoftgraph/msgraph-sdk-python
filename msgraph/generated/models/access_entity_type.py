from enum import Enum

class AccessEntityType(str, Enum):
    User = "user",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

