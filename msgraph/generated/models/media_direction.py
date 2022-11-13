from enum import Enum

class MediaDirection(Enum):
    Inactive = "inactive",
    SendOnly = "sendOnly",
    ReceiveOnly = "receiveOnly",
    SendReceive = "sendReceive",

