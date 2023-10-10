from enum import Enum

class TargettedUserType(str, Enum):
    Unknown = "unknown",
    Clicked = "clicked",
    Compromised = "compromised",
    AllUsers = "allUsers",
    UnknownFutureValue = "unknownFutureValue",

