from enum import Enum

class PackageType(str, Enum):
    Microsoft = "microsoft",
    External = "external",
    Shared = "shared",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

