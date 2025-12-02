from enum import Enum

class AiAgentPlatform(str, Enum):
    Unknown = "unknown",
    AzureAIFoundry = "azureAIFoundry",
    CopilotStudio = "copilotStudio",
    Copilot = "copilot",
    UnknownFutureValue = "unknownFutureValue",

