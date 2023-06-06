from enum import Enum

class DelegatedAdminAccessContainerType(str, Enum):
    SecurityGroup = "securityGroup",
    UnknownFutureValue = "unknownFutureValue",

