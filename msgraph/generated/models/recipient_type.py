from enum import Enum

class RecipientType(str, Enum):
    Contact = "contact",
    OneOff = "oneOff",
    Mailbox = "mailbox",
    PrivateDL = "privateDL",
    UnknownFutureValue = "unknownFutureValue",

