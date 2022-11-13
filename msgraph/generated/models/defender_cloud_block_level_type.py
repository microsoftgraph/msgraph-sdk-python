from enum import Enum

class DefenderCloudBlockLevelType(Enum):
    # Default value, uses the default Windows Defender Antivirus blocking level and provides strong detection without increasing the risk of detecting legitimate files
    NotConfigured = "notConfigured",
    # High applies a strong level of detection.
    High = "high",
    # High + uses the High level and applies addition protection measures
    HighPlus = "highPlus",
    # Zero tolerance blocks all unknown executables
    ZeroTolerance = "zeroTolerance",

