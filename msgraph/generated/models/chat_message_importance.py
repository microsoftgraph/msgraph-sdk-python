from enum import Enum

class ChatMessageImportance(Enum):
    Normal = "normal",
    High = "high",
    Urgent = "urgent",
    UnknownFutureValue = "unknownFutureValue",

