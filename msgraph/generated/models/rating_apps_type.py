from enum import Enum

class RatingAppsType(Enum):
    # Default value, allow all apps content
    AllAllowed = "allAllowed",
    # Do not allow any apps content
    AllBlocked = "allBlocked",
    # 4+, age 4 and above
    AgesAbove4 = "agesAbove4",
    # 9+, age 9 and above
    AgesAbove9 = "agesAbove9",
    # 12+, age 12 and above 
    AgesAbove12 = "agesAbove12",
    # 17+, age 17 and above
    AgesAbove17 = "agesAbove17",

