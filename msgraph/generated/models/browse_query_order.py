from enum import Enum

class BrowseQueryOrder(str, Enum):
    PathAsc = "pathAsc",
    PathDsc = "pathDsc",
    NameAsc = "nameAsc",
    NameDsc = "nameDsc",
    UnknownFutureValue = "unknownFutureValue",

