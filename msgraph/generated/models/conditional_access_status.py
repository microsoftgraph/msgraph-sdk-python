from enum import Enum

class ConditionalAccessStatus(Enum):
    Success = "success",
    Failure = "failure",
    NotApplied = "notApplied",
    UnknownFutureValue = "unknownFutureValue",

