from enum import Enum

class WindowsArchitecture(str, Enum):
    # No flags set.
    None_ = "none",
    # Whether or not the X86 Windows architecture type is supported.
    X86 = "x86",
    # Whether or not the X64 Windows architecture type is supported.
    X64 = "x64",
    # Whether or not the Arm Windows architecture type is supported.
    Arm = "arm",
    # Whether or not the Neutral Windows architecture type is supported.
    Neutral = "neutral",

