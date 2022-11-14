from enum import Enum

class RatingNewZealandTelevisionType(Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # The G classification excludes materials likely to harm children under 14
    General = "general",
    # The PGR classification encourages parents and guardians to supervise younger viewers
    ParentalGuidance = "parentalGuidance",
    # The AO classification is not suitable for children
    Adults = "adults",

