from enum import Enum

class NotificationDeliveryFrequency(str, Enum):
    Unknown = "unknown",
    Weekly = "weekly",
    BiWeekly = "biWeekly",
    UnknownFutureValue = "unknownFutureValue",

