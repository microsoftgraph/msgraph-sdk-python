from enum import Enum

class MeetingEngagementType(str, Enum):
    Reaction = "reaction",
    Hand = "hand",
    Camera = "camera",
    Microphone = "microphone",
    UnknownFutureValue = "unknownFutureValue",

