from enum import Enum

class ThreatCategory(Enum):
    Undefined = "undefined",
    Spam = "spam",
    Phishing = "phishing",
    Malware = "malware",
    UnknownFutureValue = "unknownFutureValue",

