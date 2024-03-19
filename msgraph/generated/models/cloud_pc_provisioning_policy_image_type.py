from enum import Enum

class CloudPcProvisioningPolicyImageType(str, Enum):
    Gallery = "gallery",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

