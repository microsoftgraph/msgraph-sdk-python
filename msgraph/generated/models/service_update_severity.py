from enum import Enum

class ServiceUpdateSeverity(Enum):
    Normal = "normal",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

