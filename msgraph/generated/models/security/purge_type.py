from enum import Enum

class PurgeType(str, Enum):
    Recoverable = "recoverable",
    PermanentlyDeleted = "permanentlyDeleted",
    UnknownFutureValue = "unknownFutureValue",

