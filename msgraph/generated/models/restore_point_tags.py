from enum import Enum

class RestorePointTags(str, Enum):
    None_ = "none",
    FastRestore = "fastRestore",
    UnknownFutureValue = "unknownFutureValue",

