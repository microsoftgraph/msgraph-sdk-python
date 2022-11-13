from enum import Enum

class UserPurpose(Enum):
    User = "user",
    Linked = "linked",
    Shared = "shared",
    Room = "room",
    Equipment = "equipment",
    Others = "others",
    UnknownFutureValue = "unknownFutureValue",

