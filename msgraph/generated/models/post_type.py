from enum import Enum

class PostType(str, Enum):
    Regular = "regular",
    Quick = "quick",
    Strategic = "strategic",
    UnknownFutureValue = "unknownFutureValue",

