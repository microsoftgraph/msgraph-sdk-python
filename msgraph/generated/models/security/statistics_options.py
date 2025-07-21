from enum import Enum

class StatisticsOptions(str, Enum):
    IncludeRefiners = "includeRefiners",
    IncludeQueryStats = "includeQueryStats",
    IncludeUnindexedStats = "includeUnindexedStats",
    AdvancedIndexing = "advancedIndexing",
    LocationsWithoutHits = "locationsWithoutHits",
    UnknownFutureValue = "unknownFutureValue",

