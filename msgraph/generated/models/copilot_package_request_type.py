from enum import Enum

class CopilotPackageRequestType(str, Enum):
    # A request to publish a package.
    Publish = "publish",
    # A request to activate a package.
    Activate = "activate",
    # A request to grant package access.
    Access = "access",
    # A request to update a package.
    Update = "update",
    # An evolvable sentinel for future request types.
    UnknownFutureValue = "unknownFutureValue",

