from enum import Enum

class OnboardingStatus(str, Enum):
    InsufficientInfo = "insufficientInfo",
    Onboarded = "onboarded",
    CanBeOnboarded = "canBeOnboarded",
    Unsupported = "unsupported",
    UnknownFutureValue = "unknownFutureValue",

