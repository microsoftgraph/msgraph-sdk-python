from enum import Enum

class CallType(Enum):
    Unknown = "unknown",
    GroupCall = "groupCall",
    PeerToPeer = "peerToPeer",
    UnknownFutureValue = "unknownFutureValue",

