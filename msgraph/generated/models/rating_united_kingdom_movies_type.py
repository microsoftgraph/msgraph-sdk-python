from enum import Enum

class RatingUnitedKingdomMoviesType(str, Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # The U classification is suitable for all ages
    General = "general",
    # The UC classification is suitable for pre-school children, an old rating label
    UniversalChildren = "universalChildren",
    # The PG classification is suitable for mature
    ParentalGuidance = "parentalGuidance",
    # 12, video release suitable for 12 years and over
    AgesAbove12Video = "agesAbove12Video",
    # 12A, cinema release suitable for 12 years and over
    AgesAbove12Cinema = "agesAbove12Cinema",
    # 15, suitable only for 15 years and older
    AgesAbove15 = "agesAbove15",
    # Suitable only for adults
    Adults = "adults",

