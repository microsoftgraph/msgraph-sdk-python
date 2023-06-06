from enum import Enum

class ChatMessageType(str, Enum):
    Message = "message",
    ChatEvent = "chatEvent",
    Typing = "typing",
    UnknownFutureValue = "unknownFutureValue",
    SystemEventMessage = "systemEventMessage",

