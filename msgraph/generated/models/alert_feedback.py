from enum import Enum

class AlertFeedback(Enum):
    Unknown = "unknown",
    TruePositive = "truePositive",
    FalsePositive = "falsePositive",
    BenignPositive = "benignPositive",
    UnknownFutureValue = "unknownFutureValue",

