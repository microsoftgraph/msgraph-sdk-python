from enum import Enum

class DataPolicyOperationStatus(Enum):
    NotStarted = "notStarted",
    Running = "running",
    Complete = "complete",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

