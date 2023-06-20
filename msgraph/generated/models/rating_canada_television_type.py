from enum import Enum

class RatingCanadaTelevisionType(str, Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # The C classification is suitable for children ages of 2 to 7 years
    Children = "children",
    # The C8 classification is suitable for children ages 8+
    ChildrenAbove8 = "childrenAbove8",
    # The G classification is suitable for general audience
    General = "general",
    # PG, Parental Guidance
    ParentalGuidance = "parentalGuidance",
    # The 14+ classification is intended for viewers ages 14 and older
    AgesAbove14 = "agesAbove14",
    # The 18+ classification is intended for viewers ages 18 and older
    AgesAbove18 = "agesAbove18",

