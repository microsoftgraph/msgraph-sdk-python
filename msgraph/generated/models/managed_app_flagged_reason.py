from enum import Enum

class ManagedAppFlaggedReason(Enum):
    # No issue.
    None_escaped = "none",
    # The app registration is running on a rooted/unlocked device.
    RootedDevice = "rootedDevice",

