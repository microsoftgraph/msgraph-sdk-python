from enum import Enum

class DataRetentionLevel(str, Enum):
    None_ = "none",
    DataRetained = "dataRetained",
    DeletedImmediately = "deletedImmediately",
    DeletedWithin1Month = "deletedWithin1Month",
    DeletedWithin2Weeks = "deletedWithin2Weeks",
    DeletedWithin3Months = "deletedWithin3Months",
    DeletedWithinMoreThan3Months = "deletedWithinMoreThan3Months",
    UnknownFutureValue = "unknownFutureValue",

