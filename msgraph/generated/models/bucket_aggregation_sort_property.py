from enum import Enum

class BucketAggregationSortProperty(Enum):
    Count = "count",
    KeyAsString = "keyAsString",
    KeyAsNumber = "keyAsNumber",
    UnknownFutureValue = "unknownFutureValue",

