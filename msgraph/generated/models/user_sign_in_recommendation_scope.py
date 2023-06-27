from enum import Enum

class UserSignInRecommendationScope(str, Enum):
    Tenant = "tenant",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

