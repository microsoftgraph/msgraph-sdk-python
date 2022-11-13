from enum import Enum

class WorkbookOperationStatus(Enum):
    NotStarted = "notStarted",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",

