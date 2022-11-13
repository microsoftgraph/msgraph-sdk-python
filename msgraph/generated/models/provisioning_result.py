from enum import Enum

class ProvisioningResult(Enum):
    Success = "success",
    Failure = "failure",
    Skipped = "skipped",
    Warning = "warning",
    UnknownFutureValue = "unknownFutureValue",

