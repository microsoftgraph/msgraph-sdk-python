from enum import Enum

class RestoreSessionStatus(str, Enum):
    Draft = "draft",
    Activating = "activating",
    Active = "active",
    CompletedWithError = "completedWithError",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",
    Failed = "failed",

