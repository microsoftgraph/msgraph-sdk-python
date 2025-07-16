from enum import Enum

class LayoutTemplateType(str, Enum):
    Default = "default",
    VerticalSplit = "verticalSplit",
    UnknownFutureValue = "unknownFutureValue",

