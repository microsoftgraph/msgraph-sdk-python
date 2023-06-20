from enum import Enum

class FeatureTargetType(str, Enum):
    Group = "group",
    AdministrativeUnit = "administrativeUnit",
    Role = "role",
    UnknownFutureValue = "unknownFutureValue",

