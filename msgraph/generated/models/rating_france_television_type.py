from enum import Enum

class RatingFranceTelevisionType(str, Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # The -10 classification is not recommended for children under 10
    AgesAbove10 = "agesAbove10",
    # The -12 classification is not recommended for children under 12
    AgesAbove12 = "agesAbove12",
    # The -16 classification is not recommended for children under 16
    AgesAbove16 = "agesAbove16",
    # The -18 classification is not recommended for persons under 18
    AgesAbove18 = "agesAbove18",

