from enum import Enum

class CloudPcRestorePointFrequencyType(str, Enum):
    Default = "default",
    FourHours = "fourHours",
    SixHours = "sixHours",
    TwelveHours = "twelveHours",
    SixteenHours = "sixteenHours",
    TwentyFourHours = "twentyFourHours",
    UnknownFutureValue = "unknownFutureValue",

