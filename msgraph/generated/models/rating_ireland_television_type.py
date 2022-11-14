from enum import Enum

class RatingIrelandTelevisionType(Enum):
    # Default value, allow all TV shows content
    AllAllowed = "allAllowed",
    # Do not allow any TV shows content
    AllBlocked = "allBlocked",
    # The GA classification is suitable for all audiences
    General = "general",
    # The CH classification is suitable for children
    Children = "children",
    # The YA classification is suitable for teenage audience
    YoungAdults = "youngAdults",
    # The PS classification invites parents and guardians to consider restriction children’s access
    ParentalSupervision = "parentalSupervision",
    # The MA classification is suitable for adults
    Mature = "mature",

