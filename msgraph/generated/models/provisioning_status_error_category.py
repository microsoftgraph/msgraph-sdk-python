from enum import Enum

class ProvisioningStatusErrorCategory(str, Enum):
    Failure = "failure",
    NonServiceFailure = "nonServiceFailure",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

