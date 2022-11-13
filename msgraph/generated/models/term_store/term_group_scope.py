from enum import Enum

class TermGroupScope(Enum):
    Global_escaped = "global",
    System = "system",
    SiteCollection = "siteCollection",
    UnknownFutureValue = "unknownFutureValue",

