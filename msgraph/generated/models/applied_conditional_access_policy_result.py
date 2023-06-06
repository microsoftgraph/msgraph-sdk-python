from enum import Enum

class AppliedConditionalAccessPolicyResult(str, Enum):
    Success = "success",
    Failure = "failure",
    NotApplied = "notApplied",
    NotEnabled = "notEnabled",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

