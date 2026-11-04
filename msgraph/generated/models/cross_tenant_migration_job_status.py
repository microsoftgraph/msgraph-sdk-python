from enum import Enum

class CrossTenantMigrationJobStatus(str, Enum):
    Submitted = "submitted",
    Approved = "approved",
    Processing = "processing",
    CuttingOver = "cuttingOver",
    InProgress = "inProgress",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    Failed = "failed",
    Cancelled = "cancelled",
    PendingCancel = "pendingCancel",
    AdminActionRequired = "adminActionRequired",
    ValidateSubmitted = "validateSubmitted",
    ValidateProcessing = "validateProcessing",
    ValidateInProgress = "validateInProgress",
    ValidatePassed = "validatePassed",
    ValidateFailed = "validateFailed",
    PendingDelete = "pendingDelete",
    Deleted = "deleted",
    UnknownFutureValue = "unknownFutureValue",

