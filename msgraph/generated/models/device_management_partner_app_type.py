from enum import Enum

class DeviceManagementPartnerAppType(str, Enum):
    # Partner App type is unknown.
    Unknown = "unknown",
    # Partner App is Single tenant in AAD.
    SingleTenantApp = "singleTenantApp",
    # Partner App is Multi tenant in AAD.
    MultiTenantApp = "multiTenantApp",

