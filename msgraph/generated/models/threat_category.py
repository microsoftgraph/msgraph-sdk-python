from enum import Enum

class ThreatCategory(str, Enum):
    Undefined = "undefined",
    Spam = "spam",
    Phishing = "phishing",
    Malware = "malware",
    UnknownFutureValue = "unknownFutureValue",

