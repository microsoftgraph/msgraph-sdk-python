from enum import Enum

class PrintMultipageLayout(str, Enum):
    ClockwiseFromTopLeft = "clockwiseFromTopLeft",
    CounterclockwiseFromTopLeft = "counterclockwiseFromTopLeft",
    CounterclockwiseFromTopRight = "counterclockwiseFromTopRight",
    ClockwiseFromTopRight = "clockwiseFromTopRight",
    CounterclockwiseFromBottomLeft = "counterclockwiseFromBottomLeft",
    ClockwiseFromBottomLeft = "clockwiseFromBottomLeft",
    CounterclockwiseFromBottomRight = "counterclockwiseFromBottomRight",
    ClockwiseFromBottomRight = "clockwiseFromBottomRight",
    UnknownFutureValue = "unknownFutureValue",

