from enum import Enum

class Win32LobAppRestartBehavior(str, Enum):
    # Intune will restart the device after running the app installation if the operation returns a reboot code.
    BasedOnReturnCode = "basedOnReturnCode",
    # Intune will not take any specific action on reboot codes resulting from app installations. Intune will not attempt to suppress restarts for MSI apps.
    Allow = "allow",
    # Intune will attempt to suppress restarts for MSI apps.
    Suppress = "suppress",
    # Intune will force the device to restart immediately after the app installation operation.
    Force = "force",

