from enum import Enum

class ChannelLayoutType(str, Enum):
    Post = "post",
    Chat = "chat",
    UnknownFutureValue = "unknownFutureValue",

