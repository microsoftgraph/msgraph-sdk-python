from enum import Enum

class PurgeAreas(str, Enum):
    Mailboxes = "mailboxes",
    TeamsMessages = "teamsMessages",
    UnknownFutureValue = "unknownFutureValue",

