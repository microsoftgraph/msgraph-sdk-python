from enum import Enum

class SignInFrequencyInterval(str, Enum):
    TimeBased = "timeBased",
    EveryTime = "everyTime",
    UnknownFutureValue = "unknownFutureValue",

