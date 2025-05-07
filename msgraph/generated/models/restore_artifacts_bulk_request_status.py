from enum import Enum

class RestoreArtifactsBulkRequestStatus(str, Enum):
    Unknown = "unknown",
    Active = "active",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    UnknownFutureValue = "unknownFutureValue",

