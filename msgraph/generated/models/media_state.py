from enum import Enum

class MediaState(str, Enum):
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

