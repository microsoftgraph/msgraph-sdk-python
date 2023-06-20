from enum import Enum

class WellknownListName(str, Enum):
    None_ = "none",
    DefaultList = "defaultList",
    FlaggedEmails = "flaggedEmails",
    UnknownFutureValue = "unknownFutureValue",

