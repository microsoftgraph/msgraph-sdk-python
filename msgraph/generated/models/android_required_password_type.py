from enum import Enum

class AndroidRequiredPasswordType(str, Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Alphabetic password required.
    Alphabetic = "alphabetic",
    # Alphanumeric password required.
    Alphanumeric = "alphanumeric",
    # Alphanumeric with symbols password required.
    AlphanumericWithSymbols = "alphanumericWithSymbols",
    # Low security biometrics based password required.
    LowSecurityBiometric = "lowSecurityBiometric",
    # Numeric password required.
    Numeric = "numeric",
    # Numeric complex password required.
    NumericComplex = "numericComplex",
    # A password or pattern is required, and any is acceptable.
    Any = "any",

