from enum import Enum

class RatingJapanTelevisionType(Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # All TV content is explicitly allowed
    ExplicitAllowed = "explicitAllowed",

