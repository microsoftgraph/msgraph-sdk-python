from enum import Enum

class AttributeSet(str, Enum):
    Full = "full",
    Basic = "basic",
    UnknownFutureValue = "unknownFutureValue",

