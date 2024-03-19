from enum import Enum

class TitleAreaLayoutType(str, Enum):
    ImageAndTitle = "imageAndTitle",
    Plain = "plain",
    ColorBlock = "colorBlock",
    Overlap = "overlap",
    UnknownFutureValue = "unknownFutureValue",

