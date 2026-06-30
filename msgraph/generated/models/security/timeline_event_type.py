from enum import Enum

class TimelineEventType(str, Enum):
    OriginalDelivery = "originalDelivery",
    SystemTimeTravel = "systemTimeTravel",
    DynamicDelivery = "dynamicDelivery",
    UserUrlClick = "userUrlClick",
    Reprocessed = "reprocessed",
    Zap = "zap",
    QuarantineRelease = "quarantineRelease",
    Air = "air",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

