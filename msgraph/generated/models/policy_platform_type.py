from enum import Enum

class PolicyPlatformType(str, Enum):
    # Android.
    Android = "android",
    # AndroidForWork.
    AndroidForWork = "androidForWork",
    # iOS.
    IOS = "iOS",
    # MacOS.
    MacOS = "macOS",
    # WindowsPhone 8.1.
    WindowsPhone81 = "windowsPhone81",
    # Windows 8.1 and later
    Windows81AndLater = "windows81AndLater",
    # Windows 10 and later.
    Windows10AndLater = "windows10AndLater",
    # All platforms.
    All = "all",

