from enum import Enum

class ServicePrincipalType(str, Enum):
    Unknown = "unknown",
    Application = "application",
    ManagedIdentity = "managedIdentity",
    Legacy = "legacy",
    UnknownFutureValue = "unknownFutureValue",

