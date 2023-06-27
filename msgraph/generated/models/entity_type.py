from enum import Enum

class EntityType(str, Enum):
    Event = "event",
    Message = "message",
    DriveItem = "driveItem",
    ExternalItem = "externalItem",
    Site = "site",
    List_ = "list",
    ListItem = "listItem",
    Drive = "drive",
    UnknownFutureValue = "unknownFutureValue",
    Acronym = "acronym",
    Bookmark = "bookmark",
    ChatMessage = "chatMessage",
    Person = "person",

