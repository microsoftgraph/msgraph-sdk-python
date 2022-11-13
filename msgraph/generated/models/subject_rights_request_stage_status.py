from enum import Enum

class SubjectRightsRequestStageStatus(Enum):
    NotStarted = "notStarted",
    Current = "current",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

