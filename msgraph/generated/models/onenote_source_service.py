from enum import Enum

class OnenoteSourceService(str, Enum):
    Unknown = "Unknown",
    OneDrive = "OneDrive",
    OneDriveForBusiness = "OneDriveForBusiness",
    OnPremOneDriveForBusiness = "OnPremOneDriveForBusiness",

