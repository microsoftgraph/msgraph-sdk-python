from enum import Enum

class AccessPackageSuggestionRelatedPeopleInsightLevel(str, Enum):
    Disabled = "disabled",
    Count = "count",
    CountAndNames = "countAndNames",
    UnknownFutureValue = "unknownFutureValue",

