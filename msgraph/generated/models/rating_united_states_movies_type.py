from enum import Enum

class RatingUnitedStatesMoviesType(str, Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # G, all ages admitted
    General = "general",
    # PG, some material may not be suitable for children
    ParentalGuidance = "parentalGuidance",
    # PG13, some material may be inappropriate for children under 13
    ParentalGuidance13 = "parentalGuidance13",
    # R, viewers under 17 require accompanying parent or adult guardian
    Restricted = "restricted",
    # NC17, adults only
    Adults = "adults",

