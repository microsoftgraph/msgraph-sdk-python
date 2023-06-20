from enum import Enum

class AutomaticUpdateMode(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Notify on download.
    NotifyDownload = "notifyDownload",
    # Auto-install at maintenance time.
    AutoInstallAtMaintenanceTime = "autoInstallAtMaintenanceTime",
    # Auto-install and reboot at maintenance time.
    AutoInstallAndRebootAtMaintenanceTime = "autoInstallAndRebootAtMaintenanceTime",
    # Auto-install and reboot at scheduled time.
    AutoInstallAndRebootAtScheduledTime = "autoInstallAndRebootAtScheduledTime",
    # Auto-install and restart without end-user control
    AutoInstallAndRebootWithoutEndUserControl = "autoInstallAndRebootWithoutEndUserControl",

