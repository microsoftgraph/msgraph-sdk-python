from enum import Enum

class AlertFeedback(str, Enum):
    Unknown = "unknown",
    TruePositive = "truePositive",
    FalsePositive = "falsePositive",
    BenignPositive = "benignPositive",
    UnknownFutureValue = "unknownFutureValue",

