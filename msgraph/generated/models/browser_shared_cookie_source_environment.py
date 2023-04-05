from enum import Enum

class BrowserSharedCookieSourceEnvironment(Enum):
    # Share session cookies from Microsoft Edge to Internet Explorer.
    MicrosoftEdge = "microsoftEdge",
    # Share session cookies from Internet Explorer to Microsoft Edge.
    InternetExplorer11 = "internetExplorer11",
    # Share session cookies to and from Microsoft Edge and Internet Explorer.
    Both = "both",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

