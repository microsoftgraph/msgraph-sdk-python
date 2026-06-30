from enum import Enum

class ThreatType(str, Enum):
    Unknown = "unknown",
    Spam = "spam",
    Malware = "malware",
    Phish = "phish",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

