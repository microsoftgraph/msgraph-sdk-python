from enum import Enum

class DeliveryLocation(str, Enum):
    Unknown = "unknown",
    Inbox_folder = "inbox_folder",
    JunkFolder = "junkFolder",
    DeletedFolder = "deletedFolder",
    Quarantine = "quarantine",
    Onprem_external = "onprem_external",
    Failed = "failed",
    Dropped = "dropped",
    Others = "others",
    UnknownFutureValue = "unknownFutureValue",

