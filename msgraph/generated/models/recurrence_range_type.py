from enum import Enum

class RecurrenceRangeType(str, Enum):
    EndDate = "endDate",
    NoEnd = "noEnd",
    Numbered = "numbered",

