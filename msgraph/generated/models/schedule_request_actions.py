from enum import Enum

class ScheduleRequestActions(str, Enum):
    AdminAssign = "adminAssign",
    AdminUpdate = "adminUpdate",
    AdminRemove = "adminRemove",
    SelfActivate = "selfActivate",
    SelfDeactivate = "selfDeactivate",
    AdminExtend = "adminExtend",
    AdminRenew = "adminRenew",
    SelfExtend = "selfExtend",
    SelfRenew = "selfRenew",
    UnknownFutureValue = "unknownFutureValue",

