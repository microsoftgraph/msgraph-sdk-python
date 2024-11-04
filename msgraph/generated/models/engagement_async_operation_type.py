from enum import Enum

class EngagementAsyncOperationType(str, Enum):
    # Operation to create a Viva Engage community.
    CreateCommunity = "createCommunity",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

