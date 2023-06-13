from enum import Enum

class SharedPCAccountDeletionPolicyType(str, Enum):
    # Delete immediately.
    Immediate = "immediate",
    # Delete at disk space threshold.
    DiskSpaceThreshold = "diskSpaceThreshold",
    # Delete at disk space threshold or inactive threshold.
    DiskSpaceThresholdOrInactiveThreshold = "diskSpaceThresholdOrInactiveThreshold",

