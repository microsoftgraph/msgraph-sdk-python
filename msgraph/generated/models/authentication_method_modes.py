from enum import Enum

class AuthenticationMethodModes(str, Enum):
    Password = "password",
    Voice = "voice",
    HardwareOath = "hardwareOath",
    SoftwareOath = "softwareOath",
    Sms = "sms",
    Fido2 = "fido2",
    WindowsHelloForBusiness = "windowsHelloForBusiness",
    MicrosoftAuthenticatorPush = "microsoftAuthenticatorPush",
    DeviceBasedPush = "deviceBasedPush",
    TemporaryAccessPassOneTime = "temporaryAccessPassOneTime",
    TemporaryAccessPassMultiUse = "temporaryAccessPassMultiUse",
    Email = "email",
    X509CertificateSingleFactor = "x509CertificateSingleFactor",
    X509CertificateMultiFactor = "x509CertificateMultiFactor",
    FederatedSingleFactor = "federatedSingleFactor",
    FederatedMultiFactor = "federatedMultiFactor",
    UnknownFutureValue = "unknownFutureValue",

