from enum import Enum

class ServiceUpdateCategory(Enum):
    PreventOrFixIssue = "preventOrFixIssue",
    PlanForChange = "planForChange",
    StayInformed = "stayInformed",
    UnknownFutureValue = "unknownFutureValue",

