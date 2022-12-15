from enum import Enum

class AlertStatus(Enum):
    Unknown = "unknown",
    New = "new",
    InProgress = "inProgress",
    Resolved = "resolved",
    UnknownFutureValue = "unknownFutureValue",

