from enum import Enum

class EngagementConversationModerationState(str, Enum):
    # The content is published.
    Published = "published",
    # The content is pending review by a moderator.
    PendingReview = "pendingReview",
    # he content has been rejected by a moderator.
    Dismissed = "dismissed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

