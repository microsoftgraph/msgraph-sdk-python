from enum import Enum

class InvestigationState(str, Enum):
    Unknown = "unknown",
    Terminated = "terminated",
    SuccessfullyRemediated = "successfullyRemediated",
    Benign = "benign",
    Failed = "failed",
    PartiallyRemediated = "partiallyRemediated",
    Running = "running",
    PendingApproval = "pendingApproval",
    PendingResource = "pendingResource",
    Queued = "queued",
    InnerFailure = "innerFailure",
    PreexistingAlert = "preexistingAlert",
    UnsupportedOs = "unsupportedOs",
    UnsupportedAlertType = "unsupportedAlertType",
    SuppressedAlert = "suppressedAlert",
    PartiallyInvestigated = "partiallyInvestigated",
    TerminatedByUser = "terminatedByUser",
    TerminatedBySystem = "terminatedBySystem",
    UnknownFutureValue = "unknownFutureValue",

