from enum import Enum

class RatingAustraliaMoviesType(Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # The G classification is suitable for everyone
    General = "general",
    # The PG recommends viewers under 15 with guidance from parents or guardians
    ParentalGuidance = "parentalGuidance",
    # The M classification is not recommended for viewers under 15
    Mature = "mature",
    # The MA15+ classification is not suitable for viewers under 15
    AgesAbove15 = "agesAbove15",
    # The R18+ classification is not suitable for viewers under 18
    AgesAbove18 = "agesAbove18",

