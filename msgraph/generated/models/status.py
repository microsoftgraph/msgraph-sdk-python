from enum import Enum

class Status(Enum):
    Active = "active",
    Updated = "updated",
    Deleted = "deleted",
    Ignored = "ignored",
    UnknownFutureValue = "unknownFutureValue",

