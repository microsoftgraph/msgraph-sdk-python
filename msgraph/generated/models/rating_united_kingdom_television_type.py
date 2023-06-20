from enum import Enum

class RatingUnitedKingdomTelevisionType(str, Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # Allowing TV contents with a warning message
    Caution = "caution",

