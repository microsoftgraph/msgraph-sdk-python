from enum import Enum

class RequiredPasswordType(Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Alphanumeric password required.
    Alphanumeric = "alphanumeric",
    # Numeric password required.
    Numeric = "numeric",

