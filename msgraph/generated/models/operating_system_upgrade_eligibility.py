from enum import Enum

class OperatingSystemUpgradeEligibility(str, Enum):
    # The device is upgraded to latest version of windows.
    Upgraded = "upgraded",
    # Not enough data available to compute the eligibility of device for windows upgrade.
    Unknown = "unknown",
    # The device is not capable for windows upgrade.
    NotCapable = "notCapable",
    # The device is capable for windows upgrade.
    Capable = "capable",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

