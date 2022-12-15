from enum import Enum

class EvidenceRemediationStatus(Enum):
    None_escaped = "none",
    Remediated = "remediated",
    Prevented = "prevented",
    Blocked = "blocked",
    NotFound = "notFound",
    UnknownFutureValue = "unknownFutureValue",

