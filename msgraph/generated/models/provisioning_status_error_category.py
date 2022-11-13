from enum import Enum

class ProvisioningStatusErrorCategory(Enum):
    Failure = "failure",
    NonServiceFailure = "nonServiceFailure",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

