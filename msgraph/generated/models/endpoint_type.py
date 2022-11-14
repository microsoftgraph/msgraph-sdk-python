from enum import Enum

class EndpointType(Enum):
    Default = "default",
    Voicemail = "voicemail",
    SkypeForBusiness = "skypeForBusiness",
    SkypeForBusinessVoipPhone = "skypeForBusinessVoipPhone",
    UnknownFutureValue = "unknownFutureValue",

