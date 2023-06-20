from enum import Enum

class ManagedAppDataStorageLocation(str, Enum):
    # OneDrive for business
    OneDriveForBusiness = "oneDriveForBusiness",
    # SharePoint
    SharePoint = "sharePoint",
    # Box
    Box = "box",
    # Local storage on the device
    LocalStorage = "localStorage",

