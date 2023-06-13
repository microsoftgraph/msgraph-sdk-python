from enum import Enum

class AlertStatus(str, Enum):
    Unknown = "unknown",
    NewAlert = "newAlert",
    InProgress = "inProgress",
    Resolved = "resolved",
    Dismissed = "dismissed",
    UnknownFutureValue = "unknownFutureValue",

