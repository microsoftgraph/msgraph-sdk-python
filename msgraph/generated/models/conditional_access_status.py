from enum import Enum

class ConditionalAccessStatus(str, Enum):
    Success = "success",
    Failure = "failure",
    NotApplied = "notApplied",
    UnknownFutureValue = "unknownFutureValue",

