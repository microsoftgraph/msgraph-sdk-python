from enum import Enum

class WindowsDeviceType(Enum):
    # No flags set.
    None_escaped = "none",
    # Whether or not the Desktop Windows device type is supported.
    Desktop = "desktop",
    # Whether or not the Mobile Windows device type is supported.
    Mobile = "mobile",
    # Whether or not the Holographic Windows device type is supported.
    Holographic = "holographic",
    # Whether or not the Team Windows device type is supported.
    Team = "team",

