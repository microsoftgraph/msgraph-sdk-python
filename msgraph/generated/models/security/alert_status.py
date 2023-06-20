from enum import Enum

class AlertStatus(str, Enum):
    Unknown = "unknown",
    New = "new",
    InProgress = "inProgress",
    Resolved = "resolved",
    UnknownFutureValue = "unknownFutureValue",

