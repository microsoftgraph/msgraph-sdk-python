from enum import Enum

class ExportCriteria(str, Enum):
    SearchHits = "searchHits",
    PartiallyIndexed = "partiallyIndexed",
    UnknownFutureValue = "unknownFutureValue",

