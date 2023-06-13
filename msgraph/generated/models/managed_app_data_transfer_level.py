from enum import Enum

class ManagedAppDataTransferLevel(str, Enum):
    # All apps.
    AllApps = "allApps",
    # Managed apps.
    ManagedApps = "managedApps",
    # No apps.
    None_ = "none",

