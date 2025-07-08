from enum import Enum

class ProtectionScopeState(str, Enum):
    NotModified = "notModified",
    Modified = "modified",
    UnknownFutureValue = "unknownFutureValue",

