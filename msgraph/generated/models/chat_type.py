from enum import Enum

class ChatType(Enum):
    OneOnOne = "oneOnOne",
    Group = "group",
    Meeting = "meeting",
    UnknownFutureValue = "unknownFutureValue",

