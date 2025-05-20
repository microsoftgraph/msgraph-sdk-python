from enum import Enum

class AiInteractionType(str, Enum):
    UserPrompt = "userPrompt",
    AiResponse = "aiResponse",
    UnknownFutureValue = "unknownFutureValue",

