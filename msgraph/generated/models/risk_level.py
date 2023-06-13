from enum import Enum

class RiskLevel(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Hidden = "hidden",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

