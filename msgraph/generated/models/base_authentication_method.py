from enum import Enum

class BaseAuthenticationMethod(Enum):
    Password = "password",
    Voice = "voice",
    HardwareOath = "hardwareOath",
    SoftwareOath = "softwareOath",
    Sms = "sms",
    Fido2 = "fido2",
    WindowsHelloForBusiness = "windowsHelloForBusiness",
    MicrosoftAuthenticator = "microsoftAuthenticator",
    TemporaryAccessPass = "temporaryAccessPass",
    Email = "email",
    X509Certificate = "x509Certificate",
    Federation = "federation",
    UnknownFutureValue = "unknownFutureValue",

