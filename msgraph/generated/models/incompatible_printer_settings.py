from enum import Enum

class IncompatiblePrinterSettings(str, Enum):
    Show = "show",
    Hide = "hide",
    UnknownFutureValue = "unknownFutureValue",

