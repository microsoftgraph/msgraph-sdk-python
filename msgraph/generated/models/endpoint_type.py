from enum import Enum

class EndpointType(str, Enum):
    Default = "default",
    Voicemail = "voicemail",
    SkypeForBusiness = "skypeForBusiness",
    SkypeForBusinessVoipPhone = "skypeForBusinessVoipPhone",
    UnknownFutureValue = "unknownFutureValue",

