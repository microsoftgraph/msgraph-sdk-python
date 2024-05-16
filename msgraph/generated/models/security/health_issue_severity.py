from enum import Enum

class HealthIssueSeverity(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

