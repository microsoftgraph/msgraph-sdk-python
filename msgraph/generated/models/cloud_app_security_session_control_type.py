from enum import Enum

class CloudAppSecuritySessionControlType(str, Enum):
    McasConfigured = "mcasConfigured",
    MonitorOnly = "monitorOnly",
    BlockDownloads = "blockDownloads",
    UnknownFutureValue = "unknownFutureValue",

