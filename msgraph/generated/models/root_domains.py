from enum import Enum

class RootDomains(str, Enum):
    None_ = "none",
    All = "all",
    AllFederated = "allFederated",
    AllManaged = "allManaged",
    Enumerated = "enumerated",
    AllManagedAndEnumeratedFederated = "allManagedAndEnumeratedFederated",
    UnknownFutureValue = "unknownFutureValue",

