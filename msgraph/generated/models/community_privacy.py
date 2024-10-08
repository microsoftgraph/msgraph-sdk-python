from enum import Enum

class CommunityPrivacy(str, Enum):
    # Any user from the tenant can join and participate in the community.
    Public = "public",
    # A community administrator must add tenant users to the community before they can participate.
    Private = "private",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

