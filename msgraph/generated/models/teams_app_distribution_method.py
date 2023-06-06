from enum import Enum

class TeamsAppDistributionMethod(str, Enum):
    Store = "store",
    Organization = "organization",
    Sideloaded = "sideloaded",
    UnknownFutureValue = "unknownFutureValue",

