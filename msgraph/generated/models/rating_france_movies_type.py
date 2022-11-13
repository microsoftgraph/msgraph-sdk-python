from enum import Enum

class RatingFranceMoviesType(Enum):
    # Default value, allow all movies content
    AllAllowed = "allAllowed",
    # Do not allow any movies content
    AllBlocked = "allBlocked",
    # The 10 classification prohibits the screening of the film to minors under 10
    AgesAbove10 = "agesAbove10",
    # The 12 classification prohibits the screening of the film to minors under 12
    AgesAbove12 = "agesAbove12",
    # The 16 classification prohibits the screening of the film to minors under 16
    AgesAbove16 = "agesAbove16",
    # The 18 classification prohibits the screening to minors under 18
    AgesAbove18 = "agesAbove18",

