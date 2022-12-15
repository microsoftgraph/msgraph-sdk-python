from enum import Enum

class OnboardingStatus(Enum):
    InsufficientInfo = "insufficientInfo",
    Onboarded = "onboarded",
    CanBeOnboarded = "canBeOnboarded",
    Unsupported = "unsupported",
    UnknownFutureValue = "unknownFutureValue",

