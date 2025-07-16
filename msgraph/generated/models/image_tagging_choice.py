from enum import Enum

class ImageTaggingChoice(str, Enum):
    Disabled = "disabled",
    Basic = "basic",
    Enhanced = "enhanced",
    UnknownFutureValue = "unknownFutureValue",

