from enum import Enum

class PagePromotionType(str, Enum):
    MicrosoftReserved = "microsoftReserved",
    Page = "page",
    NewsPost = "newsPost",
    UnknownFutureValue = "unknownFutureValue",

