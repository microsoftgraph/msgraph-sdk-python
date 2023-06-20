from enum import Enum

class BucketAggregationSortProperty(str, Enum):
    Count = "count",
    KeyAsString = "keyAsString",
    KeyAsNumber = "keyAsNumber",
    UnknownFutureValue = "unknownFutureValue",

