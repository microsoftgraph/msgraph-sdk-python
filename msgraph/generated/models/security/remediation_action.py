from enum import Enum

class RemediationAction(str, Enum):
    MoveToJunk = "moveToJunk",
    MoveToInbox = "moveToInbox",
    HardDelete = "hardDelete",
    SoftDelete = "softDelete",
    MoveToDeletedItems = "moveToDeletedItems",
    UnknownFutureValue = "unknownFutureValue",
    MoveToQuarantine = "moveToQuarantine",

