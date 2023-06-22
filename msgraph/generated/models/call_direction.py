from enum import Enum

class CallDirection(str, Enum):
    Incoming = "incoming",
    Outgoing = "outgoing",

