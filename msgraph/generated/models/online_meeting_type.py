from enum import Enum

class OnlineMeetingType(str, Enum):
    Adhoc = "adhoc",
    Scheduled = "scheduled",
    Recurring = "recurring",
    Broadcast = "broadcast",
    Meetnow = "meetnow",
    UnknownFutureValue = "unknownFutureValue",

