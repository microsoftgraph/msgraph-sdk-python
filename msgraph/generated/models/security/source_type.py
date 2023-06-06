from enum import Enum

class SourceType(str, Enum):
    Mailbox = "mailbox",
    Site = "site",
    UnknownFutureValue = "unknownFutureValue",

