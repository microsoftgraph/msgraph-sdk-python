from enum import Enum

class PromptLoginBehavior(str, Enum):
    TranslateToFreshPasswordAuthentication = "translateToFreshPasswordAuthentication",
    NativeSupport = "nativeSupport",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

