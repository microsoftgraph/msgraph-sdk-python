from enum import Enum

class SensorHealthStatus(str, Enum):
    Healthy = "healthy",
    NotHealthyLow = "notHealthyLow",
    NotHealthyMedium = "notHealthyMedium",
    NotHealthyHigh = "notHealthyHigh",
    UnknownFutureValue = "unknownFutureValue",

