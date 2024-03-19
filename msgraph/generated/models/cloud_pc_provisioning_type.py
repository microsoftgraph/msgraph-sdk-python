from enum import Enum

class CloudPcProvisioningType(str, Enum):
    Dedicated = "dedicated",
    Shared = "shared",
    UnknownFutureValue = "unknownFutureValue",

