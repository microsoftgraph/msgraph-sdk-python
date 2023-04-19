from enum import Enum

class ChatMessageActions(Enum):
    ReactionAdded = "reactionAdded",
    ReactionRemoved = "reactionRemoved",
    ActionUndefined = "actionUndefined",
    UnknownFutureValue = "unknownFutureValue",

