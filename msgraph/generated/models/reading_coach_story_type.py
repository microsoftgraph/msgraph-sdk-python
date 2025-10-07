from enum import Enum

class ReadingCoachStoryType(str, Enum):
    AiGenerated = "aiGenerated",
    ReadWorks = "readWorks",
    UserProvided = "userProvided",
    UnknownFutureValue = "unknownFutureValue",

