from enum import Enum

class WindowsUserAccountControlSettings(Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Always notify.
    AlwaysNotify = "alwaysNotify",
    # Notify on app changes.
    NotifyOnAppChanges = "notifyOnAppChanges",
    # Notify on app changes without dimming desktop.
    NotifyOnAppChangesWithoutDimming = "notifyOnAppChangesWithoutDimming",
    # Never notify.
    NeverNotify = "neverNotify",

