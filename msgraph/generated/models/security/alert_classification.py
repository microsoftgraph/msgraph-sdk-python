from enum import Enum

class AlertClassification(str, Enum):
    Unknown = "unknown",
    FalsePositive = "falsePositive",
    TruePositive = "truePositive",
    InformationalExpectedActivity = "informationalExpectedActivity",
    UnknownFutureValue = "unknownFutureValue",

