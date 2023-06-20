from enum import Enum

class RatingIrelandMoviesType(str, Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # Suitable for children of school going age
    General = "general",
    # The PG classification advises parental guidance
    ParentalGuidance = "parentalGuidance",
    # The 12A classification is suitable for viewers of 12 or older
    AgesAbove12 = "agesAbove12",
    # The 15A classification is suitable for viewers of 15 or older
    AgesAbove15 = "agesAbove15",
    # The 16 classification is suitable for viewers of 16 or older
    AgesAbove16 = "agesAbove16",
    # The 18 classification, suitable only for adults
    Adults = "adults",

