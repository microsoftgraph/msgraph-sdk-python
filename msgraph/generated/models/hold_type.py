from enum import Enum

class HoldType(str, Enum):
    None_ = "none",
    Private = "private",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

