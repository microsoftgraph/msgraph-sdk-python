from enum import Enum

class MicrosoftManagedDesktopType(str, Enum):
    NotManaged = "notManaged",
    PremiumManaged = "premiumManaged",
    StandardManaged = "standardManaged",
    StarterManaged = "starterManaged",
    UnknownFutureValue = "unknownFutureValue",

