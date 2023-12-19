from enum import Enum

class BehaviorDuringRetentionPeriod(str, Enum):
    DoNotRetain = "doNotRetain",
    Retain = "retain",
    RetainAsRecord = "retainAsRecord",
    RetainAsRegulatoryRecord = "retainAsRegulatoryRecord",
    UnknownFutureValue = "unknownFutureValue",

