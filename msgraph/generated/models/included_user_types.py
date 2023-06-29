from enum import Enum

class IncludedUserTypes(str, Enum):
    All = "all",
    Member = "member",
    Guest = "guest",
    UnknownFutureValue = "unknownFutureValue",

