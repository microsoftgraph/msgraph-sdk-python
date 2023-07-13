from enum import Enum

class ExportFileStructure(str, Enum):
    None_ = "none",
    Directory = "directory",
    Pst = "pst",
    UnknownFutureValue = "unknownFutureValue",

