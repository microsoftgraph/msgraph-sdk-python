from enum import Enum

class ProcessIntegrityLevel(str, Enum):
    Unknown = "unknown",
    Untrusted = "untrusted",
    Low = "low",
    Medium = "medium",
    High = "high",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

