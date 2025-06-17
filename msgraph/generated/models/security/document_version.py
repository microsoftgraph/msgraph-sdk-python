from enum import Enum

class DocumentVersion(str, Enum):
    Latest = "latest",
    Recent10 = "recent10",
    Recent100 = "recent100",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

