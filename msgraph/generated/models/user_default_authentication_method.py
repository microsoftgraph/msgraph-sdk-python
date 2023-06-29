from enum import Enum

class UserDefaultAuthenticationMethod(str, Enum):
    Push = "push",
    Oath = "oath",
    VoiceMobile = "voiceMobile",
    VoiceAlternateMobile = "voiceAlternateMobile",
    VoiceOffice = "voiceOffice",
    Sms = "sms",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

