from enum import Enum

class CoachmarkLocationType(str, Enum):
    Unknown = "unknown",
    FromEmail = "fromEmail",
    Subject = "subject",
    ExternalTag = "externalTag",
    DisplayName = "displayName",
    MessageBody = "messageBody",
    UnknownFutureValue = "unknownFutureValue",

