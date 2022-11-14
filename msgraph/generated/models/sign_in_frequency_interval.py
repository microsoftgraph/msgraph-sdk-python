from enum import Enum

class SignInFrequencyInterval(Enum):
    TimeBased = "timeBased",
    EveryTime = "everyTime",
    UnknownFutureValue = "unknownFutureValue",

