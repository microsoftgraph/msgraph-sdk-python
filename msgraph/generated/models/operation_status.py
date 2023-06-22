from enum import Enum

class OperationStatus(str, Enum):
    NotStarted = "NotStarted",
    Running = "Running",
    Completed = "Completed",
    Failed = "Failed",

