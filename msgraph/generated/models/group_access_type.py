from enum import Enum

class GroupAccessType(str, Enum):
    None_ = "none",
    Private = "private",
    Secret = "secret",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

