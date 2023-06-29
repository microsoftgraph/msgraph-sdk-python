from enum import Enum

class ContentFormat(str, Enum):
    Text = "text",
    Html = "html",
    Markdown = "markdown",
    UnknownFutureValue = "unknownFutureValue",

