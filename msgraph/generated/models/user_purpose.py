from enum import Enum

class UserPurpose(str, Enum):
    User = "user",
    Linked = "linked",
    Shared = "shared",
    Room = "room",
    Equipment = "equipment",
    Others = "others",
    UnknownFutureValue = "unknownFutureValue",

