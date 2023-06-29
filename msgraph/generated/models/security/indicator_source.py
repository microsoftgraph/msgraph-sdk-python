from enum import Enum

class IndicatorSource(str, Enum):
    Microsoft = "microsoft",
    Osint = "osint",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

