from enum import Enum

class ServiceUpdateSeverity(str, Enum):
    Normal = "normal",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

