from enum import Enum

class WindowsDeviceType(str, Enum):
    # No device types supported. Default value.
    None_ = "none",
    # Indicates support for Desktop Windows device type.
    Desktop = "desktop",
    # Indicates support for Mobile Windows device type.
    Mobile = "mobile",
    # Indicates support for Holographic Windows device type.
    Holographic = "holographic",
    # Indicates support for Team Windows device type.
    Team = "team",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

