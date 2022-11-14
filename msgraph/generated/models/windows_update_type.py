from enum import Enum

class WindowsUpdateType(Enum):
    # Allow the user to set.
    UserDefined = "userDefined",
    # Semi-annual Channel (Targeted). Device gets all applicable feature updates from Semi-annual Channel (Targeted).
    All = "all",
    # Semi-annual Channel. Device gets feature updates from Semi-annual Channel.
    BusinessReadyOnly = "businessReadyOnly",
    # Windows Insider build - Fast
    WindowsInsiderBuildFast = "windowsInsiderBuildFast",
    # Windows Insider build - Slow
    WindowsInsiderBuildSlow = "windowsInsiderBuildSlow",
    # Release Windows Insider build
    WindowsInsiderBuildRelease = "windowsInsiderBuildRelease",

