from enum import Enum

class SynchronizationTaskExecutionResult(Enum):
    Succeeded = "Succeeded",
    Failed = "Failed",
    EntryLevelErrors = "EntryLevelErrors",

