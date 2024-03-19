from enum import Enum

class SectionEmphasisType(str, Enum):
    None_ = "none",
    Neutral = "neutral",
    Soft = "soft",
    Strong = "strong",
    UnknownFutureValue = "unknownFutureValue",

