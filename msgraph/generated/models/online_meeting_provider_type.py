from enum import Enum

class OnlineMeetingProviderType(str, Enum):
    Unknown = "unknown",
    SkypeForBusiness = "skypeForBusiness",
    SkypeForConsumer = "skypeForConsumer",
    TeamsForBusiness = "teamsForBusiness",

