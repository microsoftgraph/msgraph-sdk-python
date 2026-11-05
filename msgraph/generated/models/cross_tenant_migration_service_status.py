from enum import Enum

class CrossTenantMigrationServiceStatus(str, Enum):
    NotStarted = "notStarted",
    Valid = "valid",
    Invalid = "invalid",
    Error = "error",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    Cancelled = "cancelled",
    PendingCancel = "pendingCancel",
    Syncing = "syncing",
    Synced = "synced",
    Finalizing = "finalizing",
    ForceComplete = "forceComplete",
    UnknownFutureValue = "unknownFutureValue",

