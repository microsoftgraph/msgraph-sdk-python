from enum import Enum

class CloudAppSecuritySessionControlType(Enum):
    McasConfigured = "mcasConfigured",
    MonitorOnly = "monitorOnly",
    BlockDownloads = "blockDownloads",
    UnknownFutureValue = "unknownFutureValue",

