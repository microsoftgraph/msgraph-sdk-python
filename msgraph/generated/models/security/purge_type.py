from enum import Enum

class PurgeType(str, Enum):
    Recoverable = "recoverable",
    UnknownFutureValue = "unknownFutureValue",
    PermanentlyDelete = "permanentlyDelete",

