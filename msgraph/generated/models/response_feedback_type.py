from enum import Enum

class ResponseFeedbackType(str, Enum):
    None_ = "none",
    NotDetected = "notDetected",
    VeryUnpleasant = "veryUnpleasant",
    Unpleasant = "unpleasant",
    Neutral = "neutral",
    Pleasant = "pleasant",
    VeryPleasant = "veryPleasant",
    UnknownFutureValue = "unknownFutureValue",

