from enum import Enum

class CaseType(str, Enum):
    Standard = "standard",
    Premium = "premium",
    UnknownFutureValue = "unknownFutureValue",

