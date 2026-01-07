from enum import Enum

class FileStorageContainerTypeAppPermission(str, Enum):
    None_ = "none",
    ReadContent = "readContent",
    WriteContent = "writeContent",
    ManageContent = "manageContent",
    Create = "create",
    Delete = "delete",
    Read = "read",
    Write = "write",
    EnumeratePermissions = "enumeratePermissions",
    AddPermissions = "addPermissions",
    UpdatePermissions = "updatePermissions",
    DeletePermissions = "deletePermissions",
    DeleteOwnPermission = "deleteOwnPermission",
    ManagePermissions = "managePermissions",
    Full = "full",
    UnknownFutureValue = "unknownFutureValue",

