from enum import Enum

class CheckInMethod(str, Enum):
    Unspecified = "unspecified",
    Manual = "manual",
    Inferred = "inferred",
    Verified = "verified",
    UnknownFutureValue = "unknownFutureValue",

