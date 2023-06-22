from enum import Enum

class RiskDetectionTimingType(str, Enum):
    NotDefined = "notDefined",
    Realtime = "realtime",
    NearRealtime = "nearRealtime",
    Offline = "offline",
    UnknownFutureValue = "unknownFutureValue",

