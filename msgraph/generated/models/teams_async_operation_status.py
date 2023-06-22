from enum import Enum

class TeamsAsyncOperationStatus(str, Enum):
    Invalid = "invalid",
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

