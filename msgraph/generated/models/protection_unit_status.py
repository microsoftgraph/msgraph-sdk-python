from enum import Enum

class ProtectionUnitStatus(str, Enum):
    ProtectRequested = "protectRequested",
    Protected = "protected",
    UnprotectRequested = "unprotectRequested",
    Unprotected = "unprotected",
    RemoveRequested = "removeRequested",
    UnknownFutureValue = "unknownFutureValue",

