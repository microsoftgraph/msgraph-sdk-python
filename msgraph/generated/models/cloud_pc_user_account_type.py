from enum import Enum

class CloudPcUserAccountType(str, Enum):
    StandardUser = "standardUser",
    Administrator = "administrator",
    UnknownFutureValue = "unknownFutureValue",

