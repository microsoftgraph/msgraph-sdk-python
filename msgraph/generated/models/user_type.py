from enum import Enum

class UserType(str, Enum):
    Member = "member",
    Guest = "guest",
    UnknownFutureValue = "unknownFutureValue",

