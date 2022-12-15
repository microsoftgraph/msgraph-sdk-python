from enum import Enum

class DeviceRiskScore(Enum):
    None_escaped = "none",
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

