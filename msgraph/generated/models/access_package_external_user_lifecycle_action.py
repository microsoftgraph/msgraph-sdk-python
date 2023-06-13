from enum import Enum

class AccessPackageExternalUserLifecycleAction(str, Enum):
    None_ = "none",
    BlockSignIn = "blockSignIn",
    BlockSignInAndDelete = "blockSignInAndDelete",
    UnknownFutureValue = "unknownFutureValue",

