from enum import Enum

class GiphyRatingType(str, Enum):
    Strict = "strict",
    Moderate = "moderate",
    UnknownFutureValue = "unknownFutureValue",

