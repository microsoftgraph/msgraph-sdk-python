from enum import Enum

class SynchronizationTaskExecutionResult(str, Enum):
    Succeeded = "Succeeded",
    Failed = "Failed",
    EntryLevelErrors = "EntryLevelErrors",

