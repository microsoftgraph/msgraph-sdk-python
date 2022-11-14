from enum import Enum

class ManagedAppDataTransferLevel(Enum):
    # All apps.
    AllApps = "allApps",
    # Managed apps.
    ManagedApps = "managedApps",
    # No apps.
    None_escaped = "none",

