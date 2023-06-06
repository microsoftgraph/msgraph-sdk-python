from enum import Enum

class MessageActionFlag(str, Enum):
    Any = "any",
    Call = "call",
    DoNotForward = "doNotForward",
    FollowUp = "followUp",
    Fyi = "fyi",
    Forward = "forward",
    NoResponseNecessary = "noResponseNecessary",
    Read = "read",
    Reply = "reply",
    ReplyToAll = "replyToAll",
    Review = "review",

