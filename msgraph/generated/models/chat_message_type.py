from enum import Enum

class ChatMessageType(Enum):
    Message = "message",
    ChatEvent = "chatEvent",
    Typing = "typing",
    UnknownFutureValue = "unknownFutureValue",
    SystemEventMessage = "systemEventMessage",

