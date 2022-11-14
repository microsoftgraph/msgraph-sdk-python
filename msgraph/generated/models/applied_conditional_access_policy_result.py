from enum import Enum

class AppliedConditionalAccessPolicyResult(Enum):
    Success = "success",
    Failure = "failure",
    NotApplied = "notApplied",
    NotEnabled = "notEnabled",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

