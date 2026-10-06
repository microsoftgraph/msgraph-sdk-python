from enum import Enum

class CustomCalloutExtensionType(str, Enum):
    PreApproval = "preApproval",
    PostApproval = "postApproval",
    Grant = "grant",
    Revoke = "revoke",
    UnknownFutureValue = "unknownFutureValue",

