from enum import Enum

class ExternalItemContentType(str, Enum):
    Text = "text",
    Html = "html",
    UnknownFutureValue = "unknownFutureValue",

