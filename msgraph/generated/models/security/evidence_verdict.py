from enum import Enum

class EvidenceVerdict(str, Enum):
    Unknown = "unknown",
    Suspicious = "suspicious",
    Malicious = "malicious",
    NoThreatsFound = "noThreatsFound",
    UnknownFutureValue = "unknownFutureValue",

