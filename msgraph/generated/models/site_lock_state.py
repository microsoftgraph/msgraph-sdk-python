from enum import Enum

class SiteLockState(str, Enum):
    Unlocked = "unlocked",
    LockedReadOnly = "lockedReadOnly",
    LockedNoAccess = "lockedNoAccess",
    LockedNoAdditions = "lockedNoAdditions",
    UnknownFutureValue = "unknownFutureValue",

