from enum import Enum

class WindowsStartMenuModeType(str, Enum):
    # User defined. Default value.
    UserDefined = "userDefined",
    # Full screen.
    FullScreen = "fullScreen",
    # Non-full screen.
    NonFullScreen = "nonFullScreen",

