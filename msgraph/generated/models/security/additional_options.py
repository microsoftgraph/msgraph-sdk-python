from enum import Enum

class AdditionalOptions(str, Enum):
    None_ = "none",
    TeamsAndYammerConversations = "teamsAndYammerConversations",
    CloudAttachments = "cloudAttachments",
    AllDocumentVersions = "allDocumentVersions",
    SubfolderContents = "subfolderContents",
    ListAttachments = "listAttachments",
    UnknownFutureValue = "unknownFutureValue",
    HtmlTranscripts = "htmlTranscripts",
    AdvancedIndexing = "advancedIndexing",
    AllItemsInFolder = "allItemsInFolder",
    IncludeFolderAndPath = "includeFolderAndPath",
    CondensePaths = "condensePaths",
    FriendlyName = "friendlyName",
    SplitSource = "splitSource",
    IncludeReport = "includeReport",

