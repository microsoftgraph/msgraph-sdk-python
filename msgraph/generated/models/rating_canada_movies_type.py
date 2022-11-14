from enum import Enum

class RatingCanadaMoviesType(Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # The G classification is suitable for all ages
    General = "general",
    # The PG classification advises parental guidance
    ParentalGuidance = "parentalGuidance",
    # The 14A classification is suitable for viewers above 14 or older
    AgesAbove14 = "agesAbove14",
    # The 18A classification is suitable for viewers above 18 or older
    AgesAbove18 = "agesAbove18",
    # The R classification is restricted to 18 years and older
    Restricted = "restricted",

