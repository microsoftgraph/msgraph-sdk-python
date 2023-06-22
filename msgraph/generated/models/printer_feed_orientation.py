from enum import Enum

class PrinterFeedOrientation(str, Enum):
    LongEdgeFirst = "longEdgeFirst",
    ShortEdgeFirst = "shortEdgeFirst",
    UnknownFutureValue = "unknownFutureValue",

