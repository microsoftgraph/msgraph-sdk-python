from enum import Enum

class CallType(str, Enum):
    Unknown = "unknown",
    GroupCall = "groupCall",
    PeerToPeer = "peerToPeer",
    UnknownFutureValue = "unknownFutureValue",

