from enum import Enum

class ExportFormat(str, Enum):
    Pst = "pst",
    Msg = "msg",
    Eml = "eml",
    UnknownFutureValue = "unknownFutureValue",

