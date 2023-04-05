from enum import Enum

class BrowserSiteCompatibilityMode(Enum):
    # Loads the site using default compatibility mode.
    Default = "default",
    # Loads the site in internetExplorer8 Enterprise Mode
    InternetExplorer8Enterprise = "internetExplorer8Enterprise",
    # Loads the site in internetExplorer7 Enterprise Mode
    InternetExplorer7Enterprise = "internetExplorer7Enterprise",
    # Loads the site in internetExplorer11
    InternetExplorer11 = "internetExplorer11",
    # Loads the site in internetExplorer10
    InternetExplorer10 = "internetExplorer10",
    # Loads the site in internetExplorer9
    InternetExplorer9 = "internetExplorer9",
    # Loads the site in internetExplorer8
    InternetExplorer8 = "internetExplorer8",
    # Loads the site in internetExplorer7
    InternetExplorer7 = "internetExplorer7",
    # Loads the site in internetExplorer5
    InternetExplorer5 = "internetExplorer5",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

