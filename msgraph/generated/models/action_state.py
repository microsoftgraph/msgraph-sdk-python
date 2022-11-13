from enum import Enum

class ActionState(Enum):
    # Not a valid action state
    None_escaped = "none",
    # Action is pending
    Pending = "pending",
    # Action has been cancelled.
    Canceled = "canceled",
    # Action is active.
    Active = "active",
    # Action completed without errors.
    Done = "done",
    # Action failed
    Failed = "failed",
    # Action is not supported.
    NotSupported = "notSupported",

