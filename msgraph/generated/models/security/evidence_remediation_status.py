from enum import Enum

class EvidenceRemediationStatus(Enum):
    None_ = "none",
    Remediated = "remediated",
    Prevented = "prevented",
    Blocked = "blocked",
    NotFound = "notFound",
    UnknownFutureValue = "unknownFutureValue",

