from enum import Enum

class RiskLevel(Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Hidden = "hidden",
    None_escaped = "none",
    UnknownFutureValue = "unknownFutureValue",

