from enum import Enum

class DeviceManagementSubscriptionState(str, Enum):
    # Pending
    Pending = "pending",
    # Active
    Active = "active",
    # Warning
    Warning = "warning",
    # Disabled
    Disabled = "disabled",
    # Deleted
    Deleted = "deleted",
    # Blocked
    Blocked = "blocked",
    # LockedOut
    LockedOut = "lockedOut",

