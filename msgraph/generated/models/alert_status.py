from enum import Enum

class AlertStatus(Enum):
    Unknown = "unknown",
    NewAlert = "newAlert",
    InProgress = "inProgress",
    Resolved = "resolved",
    Dismissed = "dismissed",
    UnknownFutureValue = "unknownFutureValue",

