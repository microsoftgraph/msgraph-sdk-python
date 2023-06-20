from enum import Enum

class TermGroupScope(str, Enum):
    Global_ = "global",
    System = "system",
    SiteCollection = "siteCollection",
    UnknownFutureValue = "unknownFutureValue",

