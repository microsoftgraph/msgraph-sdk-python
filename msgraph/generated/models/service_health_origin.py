from enum import Enum

class ServiceHealthOrigin(str, Enum):
    Microsoft = "microsoft",
    ThirdParty = "thirdParty",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

