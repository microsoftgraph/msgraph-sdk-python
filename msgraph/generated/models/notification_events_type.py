from enum import Enum

class NotificationEventsType(str, Enum):
    None_ = "none",
    RestoreAndPolicyUpdates = "restoreAndPolicyUpdates",
    UnknownFutureValue = "unknownFutureValue",

