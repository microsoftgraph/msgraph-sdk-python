from enum import Enum

class ConditionalAccessClientApp(Enum):
    All = "all",
    Browser = "browser",
    MobileAppsAndDesktopClients = "mobileAppsAndDesktopClients",
    ExchangeActiveSync = "exchangeActiveSync",
    EasSupported = "easSupported",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

