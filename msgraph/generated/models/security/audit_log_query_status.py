from enum import Enum

class AuditLogQueryStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    Cancelled = "cancelled",
    UnknownFutureValue = "unknownFutureValue",

