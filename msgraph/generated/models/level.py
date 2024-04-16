from enum import Enum

class Level(str, Enum):
    Beginner = "beginner",
    Intermediate = "intermediate",
    Advanced = "advanced",
    UnknownFutureValue = "unknownFutureValue",

