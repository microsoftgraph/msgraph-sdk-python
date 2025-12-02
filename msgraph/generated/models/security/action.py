from enum import Enum

class Action(str, Enum):
    Disable = "disable",
    Enable = "enable",
    ForcePasswordReset = "forcePasswordReset",
    RevokeAllSessions = "revokeAllSessions",
    RequireUserToSignInAgain = "requireUserToSignInAgain",
    MarkUserAsCompromised = "markUserAsCompromised",
    UnknownFutureValue = "unknownFutureValue",

