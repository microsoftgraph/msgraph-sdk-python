from enum import Enum

class AccessPackageExternalUserLifecycleAction(Enum):
    None_escaped = "none",
    BlockSignIn = "blockSignIn",
    BlockSignInAndDelete = "blockSignInAndDelete",
    UnknownFutureValue = "unknownFutureValue",

