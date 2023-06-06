from enum import Enum

class IncidentStatus(str, Enum):
    Active = "active",
    Resolved = "resolved",
    InProgress = "inProgress",
    Redirected = "redirected",
    UnknownFutureValue = "unknownFutureValue",
    AwaitingAction = "awaitingAction",

