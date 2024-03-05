from enum import Enum

class DriveItemSourceApplication(str, Enum):
    Teams = "teams",
    Yammer = "yammer",
    SharePoint = "sharePoint",
    OneDrive = "oneDrive",
    Stream = "stream",
    PowerPoint = "powerPoint",
    Office = "office",
    Loki = "loki",
    Loop = "loop",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

