from enum import Enum

class WindowsDeviceHealthState(str, Enum):
    # Computer is clean and no action is required
    Clean = "clean",
    # Computer is in pending full scan state
    FullScanPending = "fullScanPending",
    # Computer is in pending reboot state
    RebootPending = "rebootPending",
    # Computer is in pending manual steps state
    ManualStepsPending = "manualStepsPending",
    # Computer is in pending offline scan state
    OfflineScanPending = "offlineScanPending",
    # Computer is in critical failure state
    Critical = "critical",

