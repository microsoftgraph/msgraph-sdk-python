from enum import Enum

class UserFeedbackRating(Enum):
    NotRated = "notRated",
    Bad = "bad",
    Poor = "poor",
    Fair = "fair",
    Good = "good",
    Excellent = "excellent",
    UnknownFutureValue = "unknownFutureValue",

