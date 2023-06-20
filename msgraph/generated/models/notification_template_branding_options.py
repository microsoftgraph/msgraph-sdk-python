from enum import Enum

class NotificationTemplateBrandingOptions(str, Enum):
    # Indicates that no branding options are set in the message template.
    None_ = "none",
    # Indicates to include company logo in the message template.
    IncludeCompanyLogo = "includeCompanyLogo",
    # Indicates to include company name in the message template.
    IncludeCompanyName = "includeCompanyName",
    # Indicates to include contact information in the message template.
    IncludeContactInformation = "includeContactInformation",
    # Indicates to include company portal website link in the message template.
    IncludeCompanyPortalLink = "includeCompanyPortalLink",
    # Indicates to include device details in the message template.
    IncludeDeviceDetails = "includeDeviceDetails",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

