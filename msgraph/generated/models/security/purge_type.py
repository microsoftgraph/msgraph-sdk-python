from enum import Enum

class PurgeType(Enum):
    Recoverable = "recoverable",
    PermanentlyDeleted = "permanentlyDeleted",
    UnknownFutureValue = "unknownFutureValue",

