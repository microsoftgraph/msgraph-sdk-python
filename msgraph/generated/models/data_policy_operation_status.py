from enum import Enum

class DataPolicyOperationStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Complete = "complete",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

