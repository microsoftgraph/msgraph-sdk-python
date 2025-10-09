from enum import Enum

class ManagementState(str, Enum):
    # The device is under management
    Managed = "managed",
    # A retire command is occuring on the device and in the process of unenrolling from management
    RetirePending = "retirePending",
    # Retire command failed on the device
    RetireFailed = "retireFailed",
    # A wipe command is occuring on the device and in the process of unenrolling from management
    WipePending = "wipePending",
    # Wipe command failed on the device
    WipeFailed = "wipeFailed",
    # The device is unhealthy.
    Unhealthy = "unhealthy",
    # A delete command is occuring on the device 
    DeletePending = "deletePending",
    # A retire command was issued for the device
    RetireIssued = "retireIssued",
    # A wipe command was issued for the device
    WipeIssued = "wipeIssued",
    # A wipe command for this device has been canceled
    WipeCanceled = "wipeCanceled",
    # A retire command for this device has been canceled
    RetireCanceled = "retireCanceled",
    # The device is discovered but not fully enrolled.
    Discovered = "discovered",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

