from enum import Enum

class VerifiedIdUsageConfigurationPurpose(str, Enum):
    Recovery = "recovery",
    Onboarding = "onboarding",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

