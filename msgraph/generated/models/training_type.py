from enum import Enum

class TrainingType(str, Enum):
    Unknown = "unknown",
    Phishing = "phishing",
    UnknownFutureValue = "unknownFutureValue",

