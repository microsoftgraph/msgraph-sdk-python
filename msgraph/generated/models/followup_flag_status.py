from enum import Enum

class FollowupFlagStatus(str, Enum):
    NotFlagged = "notFlagged",
    Complete = "complete",
    Flagged = "flagged",

