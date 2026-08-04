from enum import Enum

class CustomDataProvidedResourceUploadStatus(str, Enum):
    Active = "active",
    Complete = "complete",
    Expired = "expired",
    UnknownFutureValue = "unknownFutureValue",

