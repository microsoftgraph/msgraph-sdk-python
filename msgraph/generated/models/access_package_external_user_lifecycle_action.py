from enum import Enum

class AccessPackageExternalUserLifecycleAction(Enum):
    None_ = "none",
    BlockSignIn = "blockSignIn",
    BlockSignInAndDelete = "blockSignInAndDelete",
    UnknownFutureValue = "unknownFutureValue",

