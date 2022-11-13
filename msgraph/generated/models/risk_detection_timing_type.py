from enum import Enum

class RiskDetectionTimingType(Enum):
    NotDefined = "notDefined",
    Realtime = "realtime",
    NearRealtime = "nearRealtime",
    Offline = "offline",
    UnknownFutureValue = "unknownFutureValue",

