from enum import Enum

class QueryType(str, Enum):
    Files = "files",
    Messages = "messages",
    UnknownFutureValue = "unknownFutureValue",

