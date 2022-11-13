from enum import Enum

class TeamworkCallEventType(Enum):
    Call = "call",
    Meeting = "meeting",
    ScreenShare = "screenShare",
    UnknownFutureValue = "unknownFutureValue",

