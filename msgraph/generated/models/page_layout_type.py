from enum import Enum

class PageLayoutType(str, Enum):
    MicrosoftReserved = "microsoftReserved",
    Article = "article",
    Home = "home",
    UnknownFutureValue = "unknownFutureValue",

