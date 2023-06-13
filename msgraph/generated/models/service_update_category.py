from enum import Enum

class ServiceUpdateCategory(str, Enum):
    PreventOrFixIssue = "preventOrFixIssue",
    PlanForChange = "planForChange",
    StayInformed = "stayInformed",
    UnknownFutureValue = "unknownFutureValue",

