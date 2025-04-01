from enum import Enum

class ItemsToInclude(str, Enum):
    SearchHits = "searchHits",
    PartiallyIndexed = "partiallyIndexed",
    UnknownFutureValue = "unknownFutureValue",

