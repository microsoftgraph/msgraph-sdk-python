from enum import Enum

class PayloadComplexity(str, Enum):
    Unknown = "unknown",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

