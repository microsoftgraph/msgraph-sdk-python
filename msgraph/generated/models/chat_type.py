from enum import Enum

class ChatType(str, Enum):
    OneOnOne = "oneOnOne",
    Group = "group",
    Meeting = "meeting",
    UnknownFutureValue = "unknownFutureValue",

