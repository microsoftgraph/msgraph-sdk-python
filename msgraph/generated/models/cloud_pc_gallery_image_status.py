from enum import Enum

class CloudPcGalleryImageStatus(str, Enum):
    Supported = "supported",
    SupportedWithWarning = "supportedWithWarning",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

