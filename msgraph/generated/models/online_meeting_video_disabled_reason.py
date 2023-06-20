from enum import Enum

class OnlineMeetingVideoDisabledReason(str, Enum):
    WatermarkProtection = "watermarkProtection",
    UnknownFutureValue = "unknownFutureValue",

