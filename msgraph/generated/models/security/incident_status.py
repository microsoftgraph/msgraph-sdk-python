from enum import Enum

class IncidentStatus(Enum):
    Active = "active",
    Resolved = "resolved",
    InProgress = "inProgress",
    Redirected = "redirected",
    UnknownFutureValue = "unknownFutureValue",

