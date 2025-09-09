from enum import Enum

class ManagedAppDataStorageLocation(str, Enum):
    # Indicates allowed storage location for the managed app to save files is 'OneDrive for Business'.
    OneDriveForBusiness = "oneDriveForBusiness",
    # Indicates allowed storage location for the managed app to save files is 'Sharepoint'.
    SharePoint = "sharePoint",
    # Indicates that the allowed storage location for a managed app to save files is to 'Box'. Box is a non-Microsoft solution that enables cloud-based file storage capabilities.
    Box = "box",
    # Indicates allowed storage location for the managed app to save files is local storage on the device.
    LocalStorage = "localStorage",

