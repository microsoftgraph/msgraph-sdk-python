from enum import Enum

class ProvisioningAction(str, Enum):
    Other = "other",
    Create = "create",
    Delete = "delete",
    Disable = "disable",
    Update = "update",
    StagedDelete = "stagedDelete",
    UnknownFutureValue = "unknownFutureValue",

