from enum import Enum

class EntityType(Enum):
    Event = "event",
    Message = "message",
    DriveItem = "driveItem",
    ExternalItem = "externalItem",
    Site = "site",
    List = "list",
    ListItem = "listItem",
    Drive = "drive",
    UnknownFutureValue = "unknownFutureValue",

