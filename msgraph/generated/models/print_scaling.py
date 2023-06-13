from enum import Enum

class PrintScaling(str, Enum):
    Auto = "auto",
    ShrinkToFit = "shrinkToFit",
    Fill = "fill",
    Fit = "fit",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

