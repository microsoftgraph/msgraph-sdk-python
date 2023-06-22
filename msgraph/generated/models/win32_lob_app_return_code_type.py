from enum import Enum

class Win32LobAppReturnCodeType(str, Enum):
    # Failed.
    Failed = "failed",
    # Success.
    Success = "success",
    # Soft-reboot is required.
    SoftReboot = "softReboot",
    # Hard-reboot is required.
    HardReboot = "hardReboot",
    # Retry.
    Retry = "retry",

