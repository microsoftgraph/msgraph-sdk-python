from enum import Enum

class ConditionalAccessClientApp(str, Enum):
    All = "all",
    Browser = "browser",
    MobileAppsAndDesktopClients = "mobileAppsAndDesktopClients",
    ExchangeActiveSync = "exchangeActiveSync",
    EasSupported = "easSupported",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

