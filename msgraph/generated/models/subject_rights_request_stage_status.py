from enum import Enum

class SubjectRightsRequestStageStatus(str, Enum):
    NotStarted = "notStarted",
    Current = "current",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

