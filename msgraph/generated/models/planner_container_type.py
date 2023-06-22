from enum import Enum

class PlannerContainerType(str, Enum):
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",
    Roster = "roster",

