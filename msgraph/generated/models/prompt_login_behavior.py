from enum import Enum

class PromptLoginBehavior(Enum):
    TranslateToFreshPasswordAuthentication = "translateToFreshPasswordAuthentication",
    NativeSupport = "nativeSupport",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

