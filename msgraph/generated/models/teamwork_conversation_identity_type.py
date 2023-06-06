from enum import Enum

class TeamworkConversationIdentityType(str, Enum):
    Team = "team",
    Channel = "channel",
    Chat = "chat",
    UnknownFutureValue = "unknownFutureValue",

