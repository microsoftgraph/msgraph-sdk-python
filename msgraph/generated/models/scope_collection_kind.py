from enum import Enum

class ScopeCollectionKind(str, Enum):
    AllAllowed = "allAllowed",
    Enumerated = "enumerated",
    None_ = "none",
    ScopeKindNotSet = "scopeKindNotSet",
    UnknownFutureValue = "unknownFutureValue",

