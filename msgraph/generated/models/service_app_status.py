from enum import Enum

class ServiceAppStatus(str, Enum):
    Inactive = "inactive",
    Active = "active",
    PendingActive = "pendingActive",
    PendingInactive = "pendingInactive",
    UnknownFutureValue = "unknownFutureValue",

