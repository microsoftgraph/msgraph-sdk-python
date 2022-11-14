from enum import Enum

class OperationResult(Enum):
    Success = "success",
    Failure = "failure",
    Timeout = "timeout",
    UnknownFutureValue = "unknownFutureValue",

