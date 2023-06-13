from enum import Enum

class SearchContent(str, Enum):
    SharedContent = "sharedContent",
    PrivateContent = "privateContent",
    UnknownFutureValue = "unknownFutureValue",

