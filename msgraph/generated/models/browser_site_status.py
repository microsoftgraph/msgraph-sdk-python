from enum import Enum

class BrowserSiteStatus(Enum):
    # A site that has been published
    Published = "published",
    # A site that has been added pending publish
    PendingAdd = "pendingAdd",
    # A site that has been edited pending publish
    PendingEdit = "pendingEdit",
    # A site that has been deleted pending publish
    PendingDelete = "pendingDelete",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

