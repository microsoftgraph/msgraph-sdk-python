from enum import Enum

class ChatMessageImportance(str, Enum):
    Normal = "normal",
    High = "high",
    Urgent = "urgent",
    UnknownFutureValue = "unknownFutureValue",

