from enum import Enum

class TeamsAsyncOperationStatus(Enum):
    Invalid = "invalid",
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

