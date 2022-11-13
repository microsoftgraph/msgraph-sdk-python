from enum import Enum

class RatingJapanMoviesType(Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # Suitable for all ages
    General = "general",
    # The PG-12 classification requests parental guidance for young people under 12
    ParentalGuidance = "parentalGuidance",
    # The R15+ classification is suitable for viewers of 15 or older
    AgesAbove15 = "agesAbove15",
    # The R18+ classification is suitable for viewers of 18 or older
    AgesAbove18 = "agesAbove18",

