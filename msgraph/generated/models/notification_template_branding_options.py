from enum import Enum

class NotificationTemplateBrandingOptions(Enum):
    # No Branding.
    None_escaped = "none",
    # Include Company Logo.
    IncludeCompanyLogo = "includeCompanyLogo",
    # Include Company Name.
    IncludeCompanyName = "includeCompanyName",
    # Include Contact Info.
    IncludeContactInformation = "includeContactInformation",
    # Include Company Portal Link.
    IncludeCompanyPortalLink = "includeCompanyPortalLink",
    # Include Device Details.
    IncludeDeviceDetails = "includeDeviceDetails",

