from enum import Enum

class PrintOrientation(str, Enum):
    Portrait = "portrait",
    Landscape = "landscape",
    ReverseLandscape = "reverseLandscape",
    ReversePortrait = "reversePortrait",
    UnknownFutureValue = "unknownFutureValue",

