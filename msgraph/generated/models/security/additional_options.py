from enum import Enum

class AdditionalOptions(str, Enum):
    None_ = "none",
    TeamsAndYammerConversations = "teamsAndYammerConversations",
    CloudAttachments = "cloudAttachments",
    AllDocumentVersions = "allDocumentVersions",
    SubfolderContents = "subfolderContents",
    ListAttachments = "listAttachments",
    UnknownFutureValue = "unknownFutureValue",

