from enum import Enum

class PrintFinishing(str, Enum):
    None_ = "none",
    Staple = "staple",
    Punch = "punch",
    Cover = "cover",
    Bind = "bind",
    SaddleStitch = "saddleStitch",
    StitchEdge = "stitchEdge",
    StapleTopLeft = "stapleTopLeft",
    StapleBottomLeft = "stapleBottomLeft",
    StapleTopRight = "stapleTopRight",
    StapleBottomRight = "stapleBottomRight",
    StitchLeftEdge = "stitchLeftEdge",
    StitchTopEdge = "stitchTopEdge",
    StitchRightEdge = "stitchRightEdge",
    StitchBottomEdge = "stitchBottomEdge",
    StapleDualLeft = "stapleDualLeft",
    StapleDualTop = "stapleDualTop",
    StapleDualRight = "stapleDualRight",
    StapleDualBottom = "stapleDualBottom",
    UnknownFutureValue = "unknownFutureValue",

