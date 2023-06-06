from enum import Enum

class OperationResult(str, Enum):
    Success = "success",
    Failure = "failure",
    Timeout = "timeout",
    UnknownFutureValue = "unknownFutureValue",

