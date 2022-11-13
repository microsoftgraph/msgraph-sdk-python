from enum import Enum

class OperationStatus(Enum):
    NotStarted = "NotStarted",
    Running = "Running",
    Completed = "Completed",
    Failed = "Failed",

