from enum import Enum

class BrowserSiteTargetEnvironment(str, Enum):
    # Open in Internet Explorer Mode
    InternetExplorerMode = "internetExplorerMode",
    # Open in standalone Internet Explorer 11
    InternetExplorer11 = "internetExplorer11",
    # Open in Microsoft Edge
    MicrosoftEdge = "microsoftEdge",
    # Configurable type
    Configurable = "configurable",
    # Open in the browser the employee chooses.
    None_ = "none",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

