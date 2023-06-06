from enum import Enum

class BrowserSiteListStatus(str, Enum):
    # A site list that has not yet been published
    Draft = "draft",
    # A site list that has been published with no pending changes.
    Published = "published",
    # A site that has pending changes
    Pending = "pending",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shoudn't be necessary.
    UnknownFutureValue = "unknownFutureValue",

