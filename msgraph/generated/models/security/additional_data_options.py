from enum import Enum

class AdditionalDataOptions(str, Enum):
    AllVersions = "allVersions",
    LinkedFiles = "linkedFiles",
    UnknownFutureValue = "unknownFutureValue",
    AdvancedIndexing = "advancedIndexing",
    ListAttachments = "listAttachments",
    HtmlTranscripts = "htmlTranscripts",
    MessageConversationExpansion = "messageConversationExpansion",
    LocationsWithoutHits = "locationsWithoutHits",
    AllItemsInFolder = "allItemsInFolder",

