from enum import Enum

class VppTokenSyncStatus(Enum):
    # Default status.
    None_ = "none",
    # Last Sync in progress.
    InProgress = "inProgress",
    # Last Sync completed successfully.
    Completed = "completed",
    # Last Sync failed.
    Failed = "failed",

