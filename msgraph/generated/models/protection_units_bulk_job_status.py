from enum import Enum

class ProtectionUnitsBulkJobStatus(str, Enum):
    Unknown = "unknown",
    Active = "active",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    UnknownFutureValue = "unknownFutureValue",

