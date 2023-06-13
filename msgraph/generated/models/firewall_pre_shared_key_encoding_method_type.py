from enum import Enum

class FirewallPreSharedKeyEncodingMethodType(str, Enum):
    # No value configured by Intune, do not override the user-configured device default value
    DeviceDefault = "deviceDefault",
    # Preshared key is not encoded. Instead, it is kept in its wide-character format
    None_ = "none",
    # Encode the preshared key using UTF-8
    UtF8 = "utF8",

