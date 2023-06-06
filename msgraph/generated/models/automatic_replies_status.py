from enum import Enum

class AutomaticRepliesStatus(str, Enum):
    Disabled = "disabled",
    AlwaysEnabled = "alwaysEnabled",
    Scheduled = "scheduled",

