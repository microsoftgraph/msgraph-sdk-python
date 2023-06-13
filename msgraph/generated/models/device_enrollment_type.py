from enum import Enum

class DeviceEnrollmentType(str, Enum):
    # Default value, enrollment type was not collected.
    Unknown = "unknown",
    # User driven enrollment through BYOD channel.
    UserEnrollment = "userEnrollment",
    # User enrollment with a device enrollment manager account.
    DeviceEnrollmentManager = "deviceEnrollmentManager",
    # Apple bulk enrollment with user challenge. (DEP, Apple Configurator)
    AppleBulkWithUser = "appleBulkWithUser",
    # Apple bulk enrollment without user challenge. (DEP, Apple Configurator, Mobile Config)
    AppleBulkWithoutUser = "appleBulkWithoutUser",
    # Windows 10 Azure AD Join.
    WindowsAzureADJoin = "windowsAzureADJoin",
    # Windows 10 Bulk enrollment through ICD with certificate.
    WindowsBulkUserless = "windowsBulkUserless",
    # Windows 10 automatic enrollment. (Add work account)
    WindowsAutoEnrollment = "windowsAutoEnrollment",
    # Windows 10 bulk Azure AD Join.
    WindowsBulkAzureDomainJoin = "windowsBulkAzureDomainJoin",
    # Windows 10 Co-Management triggered by AutoPilot or Group Policy.
    WindowsCoManagement = "windowsCoManagement",
    # Windows 10 Azure AD Join using Device Auth.
    WindowsAzureADJoinUsingDeviceAuth = "windowsAzureADJoinUsingDeviceAuth",
    # Device managed by Apple user enrollment
    AppleUserEnrollment = "appleUserEnrollment",
    # Device managed by Apple user enrollment with service account
    AppleUserEnrollmentWithServiceAccount = "appleUserEnrollmentWithServiceAccount",

