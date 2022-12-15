from enum import Enum

class AlertClassification(Enum):
    Unknown = "unknown",
    FalsePositive = "falsePositive",
    TruePositive = "truePositive",
    InformationalExpectedActivity = "informationalExpectedActivity",
    UnknownFutureValue = "unknownFutureValue",

