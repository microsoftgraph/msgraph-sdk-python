from enum import Enum

class IncidentStatus(Enum):
    Active = "active",
    Resolved = "resolved",
    Redirected = "redirected",
    UnknownFutureValue = "unknownFutureValue",

