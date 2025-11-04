from enum import Enum

class WebApplicationFirewallVerificationStatus(str, Enum):
    Success = "success",
    Warning = "warning",
    Failure = "failure",
    UnknownFutureValue = "unknownFutureValue",

