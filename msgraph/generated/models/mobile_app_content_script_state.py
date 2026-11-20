from enum import Enum

class MobileAppContentScriptState(str, Enum):
    # Indicates that the script content is in a pending state.
    CommitPending = "commitPending",
    # Indicates that the script content is ready.
    CommitSuccess = "commitSuccess",
    # Indicates that the script is in an unusable state.
    CommitFailed = "commitFailed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

