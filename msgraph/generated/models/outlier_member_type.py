from enum import Enum

class OutlierMemberType(str, Enum):
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

