from enum import Enum

class RatingNewZealandMoviesType(str, Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # Suitable for general audience
    General = "general",
    # The PG classification recommends parental guidance
    ParentalGuidance = "parentalGuidance",
    # The M classification is suitable for mature audience
    Mature = "mature",
    # The R13 classification is restricted to persons 13 years and over
    AgesAbove13 = "agesAbove13",
    # The R15 classification is restricted to persons 15 years and over
    AgesAbove15 = "agesAbove15",
    # The R16 classification is restricted to persons 16 years and over
    AgesAbove16 = "agesAbove16",
    # The R18 classification is restricted to persons 18 years and over
    AgesAbove18 = "agesAbove18",
    # The R classification is restricted to a certain audience
    Restricted = "restricted",
    # The RP16 classification requires viewers under 16 accompanied by a parent or an adult
    AgesAbove16Restricted = "agesAbove16Restricted",

