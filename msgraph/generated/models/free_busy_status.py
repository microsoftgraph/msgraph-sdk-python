from enum import Enum

class FreeBusyStatus(str, Enum):
    Unknown = "unknown",
    Free = "free",
    Tentative = "tentative",
    Busy = "busy",
    Oof = "oof",
    WorkingElsewhere = "workingElsewhere",

