from enum import Enum

class Win32LobAppMsiPackageType(str, Enum):
    # Indicates a per-machine app package.
    PerMachine = "perMachine",
    # Indicates a per-user app package.
    PerUser = "perUser",
    # Indicates a dual-purpose app package.
    DualPurpose = "dualPurpose",

