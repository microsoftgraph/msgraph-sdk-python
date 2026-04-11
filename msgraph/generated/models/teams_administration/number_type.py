from enum import Enum

class NumberType(str, Enum):
    InternalError = "internalError",
    DirectRouting = "directRouting",
    CallingPlan = "callingPlan",
    OperatorConnect = "operatorConnect",
    UnknownFutureValue = "unknownFutureValue",

