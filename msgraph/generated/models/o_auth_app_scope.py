from enum import Enum

class OAuthAppScope(str, Enum):
    Unknown = "unknown",
    ReadCalendar = "readCalendar",
    ReadContact = "readContact",
    ReadMail = "readMail",
    ReadAllChat = "readAllChat",
    ReadAllFile = "readAllFile",
    ReadAndWriteMail = "readAndWriteMail",
    SendMail = "sendMail",
    UnknownFutureValue = "unknownFutureValue",

