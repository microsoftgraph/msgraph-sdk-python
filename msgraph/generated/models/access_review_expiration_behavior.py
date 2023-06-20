from enum import Enum

class AccessReviewExpirationBehavior(str, Enum):
    KeepAccess = "keepAccess",
    RemoveAccess = "removeAccess",
    AcceptAccessRecommendation = "acceptAccessRecommendation",
    UnknownFutureValue = "unknownFutureValue",

