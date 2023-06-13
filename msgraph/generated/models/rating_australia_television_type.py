from enum import Enum

class RatingAustraliaTelevisionType(str, Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # The P classification is intended for preschoolers
    Preschoolers = "preschoolers",
    # The C classification is intended for children under 14
    Children = "children",
    # The G classification is suitable for all ages
    General = "general",
    # The PG classification is recommended for young viewers
    ParentalGuidance = "parentalGuidance",
    # The M classification is recommended for viewers over 15
    Mature = "mature",
    # The MA15+ classification is not suitable for viewers under 15
    AgesAbove15 = "agesAbove15",
    # The AV15+ classification is not suitable for viewers under 15, adult violence-specific
    AgesAbove15AdultViolence = "agesAbove15AdultViolence",

