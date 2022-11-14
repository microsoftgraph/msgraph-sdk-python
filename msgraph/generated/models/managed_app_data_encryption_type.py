from enum import Enum

class ManagedAppDataEncryptionType(Enum):
    # App data is encrypted based on the default settings on the device.
    UseDeviceSettings = "useDeviceSettings",
    # App data is encrypted when the device is restarted.
    AfterDeviceRestart = "afterDeviceRestart",
    # App data associated with this policy is encrypted when the device is locked, except data in files that are open
    WhenDeviceLockedExceptOpenFiles = "whenDeviceLockedExceptOpenFiles",
    # App data associated with this policy is encrypted when the device is locked
    WhenDeviceLocked = "whenDeviceLocked",

