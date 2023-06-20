from enum import Enum

class PrintColorMode(str, Enum):
    BlackAndWhite = "blackAndWhite",
    Grayscale = "grayscale",
    Color = "color",
    Auto = "auto",
    UnknownFutureValue = "unknownFutureValue",

