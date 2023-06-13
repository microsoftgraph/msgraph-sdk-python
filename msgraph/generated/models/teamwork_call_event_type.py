from enum import Enum

class TeamworkCallEventType(str, Enum):
    Call = "call",
    Meeting = "meeting",
    ScreenShare = "screenShare",
    UnknownFutureValue = "unknownFutureValue",

