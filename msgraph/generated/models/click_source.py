from enum import Enum

class ClickSource(str, Enum):
    Unknown = "unknown",
    QrCode = "qrCode",
    PhishingUrl = "phishingUrl",
    UnknownFutureValue = "unknownFutureValue",

