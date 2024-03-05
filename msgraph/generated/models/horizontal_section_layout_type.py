from enum import Enum

class HorizontalSectionLayoutType(str, Enum):
    None_ = "none",
    OneColumn = "oneColumn",
    TwoColumns = "twoColumns",
    ThreeColumns = "threeColumns",
    OneThirdLeftColumn = "oneThirdLeftColumn",
    OneThirdRightColumn = "oneThirdRightColumn",
    FullWidth = "fullWidth",
    UnknownFutureValue = "unknownFutureValue",

