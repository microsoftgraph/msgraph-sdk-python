from enum import Enum

class Status(str, Enum):
    Active = "active",
    Updated = "updated",
    Deleted = "deleted",
    Ignored = "ignored",
    UnknownFutureValue = "unknownFutureValue",

