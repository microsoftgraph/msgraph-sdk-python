from enum import Enum

class MicrosoftAuthenticatorAuthenticationMode(str, Enum):
    DeviceBasedPush = "deviceBasedPush",
    Push = "push",
    Any = "any",

