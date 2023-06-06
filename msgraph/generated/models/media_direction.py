from enum import Enum

class MediaDirection(str, Enum):
    Inactive = "inactive",
    SendOnly = "sendOnly",
    ReceiveOnly = "receiveOnly",
    SendReceive = "sendReceive",

