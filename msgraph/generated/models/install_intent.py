from enum import Enum

class InstallIntent(str, Enum):
    # Available install intent.
    Available = "available",
    # Required install intent.
    Required = "required",
    # Uninstall install intent.
    Uninstall = "uninstall",
    # Available without enrollment install intent.
    AvailableWithoutEnrollment = "availableWithoutEnrollment",

