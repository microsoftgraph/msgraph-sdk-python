from enum import Enum

class ChatMessageActions(str, Enum):
    ReactionAdded = "reactionAdded",
    ReactionRemoved = "reactionRemoved",
    ActionUndefined = "actionUndefined",
    UnknownFutureValue = "unknownFutureValue",

