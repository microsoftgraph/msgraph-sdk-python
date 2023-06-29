from enum import Enum

class SignInUserType(str, Enum):
    Member = "member",
    Guest = "guest",
    UnknownFutureValue = "unknownFutureValue",

