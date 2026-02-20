from enum import Enum

class ResourceAccessStatus(str, Enum):
    None_ = "none",
    Failure = "failure",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

