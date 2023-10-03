from enum import Enum

class EndUserNotificationPreference(str, Enum):
    Unknown = "unknown",
    Microsoft = "microsoft",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

