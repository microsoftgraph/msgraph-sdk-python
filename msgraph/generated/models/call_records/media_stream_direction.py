from enum import Enum

class MediaStreamDirection(str, Enum):
    CallerToCallee = "callerToCallee",
    CalleeToCaller = "calleeToCaller",

