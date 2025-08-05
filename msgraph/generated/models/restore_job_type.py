from enum import Enum

class RestoreJobType(str, Enum):
    Standard = "standard",
    Bulk = "bulk",
    UnknownFutureValue = "unknownFutureValue",

