from enum import Enum

class SiteArchiveStatus(str, Enum):
    RecentlyArchived = "recentlyArchived",
    FullyArchived = "fullyArchived",
    Reactivating = "reactivating",
    UnknownFutureValue = "unknownFutureValue",

