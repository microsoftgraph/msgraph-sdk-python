from enum import Enum

class ServiceHealthOrigin(Enum):
    Microsoft = "microsoft",
    ThirdParty = "thirdParty",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

