from enum import Enum

class UserAction(str, Enum):
    RegisterSecurityInformation = "registerSecurityInformation",
    RegisterOrJoinDevices = "registerOrJoinDevices",
    UnknownFutureValue = "unknownFutureValue",

