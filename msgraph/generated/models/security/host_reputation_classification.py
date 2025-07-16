from enum import Enum

class HostReputationClassification(str, Enum):
    Unknown = "unknown",
    Neutral = "neutral",
    Suspicious = "suspicious",
    Malicious = "malicious",
    UnknownFutureValue = "unknownFutureValue",

