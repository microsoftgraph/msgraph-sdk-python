from enum import Enum

class ProvisioningResult(str, Enum):
    Success = "success",
    Failure = "failure",
    Skipped = "skipped",
    Warning = "warning",
    UnknownFutureValue = "unknownFutureValue",

