from enum import Enum

class FreeBusyStatus(Enum):
    Unknown = "unknown",
    Free = "free",
    Tentative = "tentative",
    Busy = "busy",
    Oof = "oof",
    WorkingElsewhere = "workingElsewhere",

