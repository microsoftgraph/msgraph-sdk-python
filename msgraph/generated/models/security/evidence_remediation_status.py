from enum import Enum

class EvidenceRemediationStatus(str, Enum):
    None_ = "none",
    Remediated = "remediated",
    Prevented = "prevented",
    Blocked = "blocked",
    NotFound = "notFound",
    UnknownFutureValue = "unknownFutureValue",
    Active = "active",
    PendingApproval = "pendingApproval",
    Declined = "declined",
    Unremediated = "unremediated",
    Running = "running",
    PartiallyRemediated = "partiallyRemediated",

