from enum import Enum

class BrowserSiteMergeType(Enum):
    # No merge type
    NoMerge = "noMerge",
    # Default merge type
    Default = "default",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

