from enum import Enum

class RatingUnitedStatesTelevisionType(Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # TV-Y, all children
    ChildrenAll = "childrenAll",
    # TV-Y7, children age 7 and above
    ChildrenAbove7 = "childrenAbove7",
    # TV-G, suitable for all ages
    General = "general",
    # TV-PG, parental guidance
    ParentalGuidance = "parentalGuidance",
    # TV-14, children age 14 and above
    ChildrenAbove14 = "childrenAbove14",
    # TV-MA, adults only
    Adults = "adults",

