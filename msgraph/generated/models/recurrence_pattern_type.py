from enum import Enum

class RecurrencePatternType(Enum):
    Daily = "daily",
    Weekly = "weekly",
    AbsoluteMonthly = "absoluteMonthly",
    RelativeMonthly = "relativeMonthly",
    AbsoluteYearly = "absoluteYearly",
    RelativeYearly = "relativeYearly",

