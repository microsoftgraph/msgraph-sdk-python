from enum import Enum

class HealthIssueStatus(str, Enum):
    Open = "open",
    Closed = "closed",
    Suppressed = "suppressed",
    UnknownFutureValue = "unknownFutureValue",

