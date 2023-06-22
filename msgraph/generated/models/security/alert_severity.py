from enum import Enum

class AlertSeverity(str, Enum):
    Unknown = "unknown",
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

