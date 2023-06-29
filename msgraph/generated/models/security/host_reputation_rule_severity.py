from enum import Enum

class HostReputationRuleSeverity(str, Enum):
    Unknown = "unknown",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

