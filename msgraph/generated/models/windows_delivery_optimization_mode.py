from enum import Enum

class WindowsDeliveryOptimizationMode(str, Enum):
    # Allow the user to set.
    UserDefined = "userDefined",
    # HTTP only, no peering
    HttpOnly = "httpOnly",
    # OS default – Http blended with peering behind the same network address translator
    HttpWithPeeringNat = "httpWithPeeringNat",
    # HTTP blended with peering across a private group
    HttpWithPeeringPrivateGroup = "httpWithPeeringPrivateGroup",
    # HTTP blended with Internet peering
    HttpWithInternetPeering = "httpWithInternetPeering",
    # Simple download mode with no peering
    SimpleDownload = "simpleDownload",
    # Bypass mode. Do not use Delivery Optimization and use BITS instead
    BypassMode = "bypassMode",

