from enum import Enum

class RestorePointPreference(str, Enum):
    Latest = "latest",
    Oldest = "oldest",
    UnknownFutureValue = "unknownFutureValue",

