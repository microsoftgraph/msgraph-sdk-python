from enum import Enum

class EvidenceVerdict(Enum):
    Unknown = "unknown",
    Suspicious = "suspicious",
    Malicious = "malicious",
    NoThreatsFound = "noThreatsFound",
    UnknownFutureValue = "unknownFutureValue",

