from enum import Enum

class ManagedDevicePartnerReportedHealthState(Enum):
    # Device health state is not yet reported
    Unknown = "unknown",
    # Device has been activated by a mobile threat defense partner, but has not yet reported health.
    Activated = "activated",
    # Device has been deactivated by a mobile threat defense partner. The device health is not known.
    Deactivated = "deactivated",
    # Device is considered secured by the mobile threat defense partner.
    Secured = "secured",
    # Device is considered low threat by the mobile threat defense partner.
    LowSeverity = "lowSeverity",
    # Device is considered medium threat by the mobile threat defense partner.
    MediumSeverity = "mediumSeverity",
    # Device is considered high threat by the mobile threat defense partner.
    HighSeverity = "highSeverity",
    # Device is considered unresponsive by the mobile threat defense partner. The device health is not known.
    Unresponsive = "unresponsive",
    # Device is considered compromised by the Threat Defense partner. This means the device has an active Threat or Risk which cannot be easily remediated by the end user and the user should contact their IT Admin.
    Compromised = "compromised",
    # Device is considered misconfigured with the Threat Defense partner. This means the device is missing a required profile or configuration for the Threat Defense Partner to function properly and is thus threat or risk analysis is not able to complete.
    Misconfigured = "misconfigured",

