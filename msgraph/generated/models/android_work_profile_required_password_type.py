from enum import Enum

class AndroidWorkProfileRequiredPasswordType(str, Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Low security biometrics based password required.
    LowSecurityBiometric = "lowSecurityBiometric",
    # Required.
    Required = "required",
    # At least numeric password required.
    AtLeastNumeric = "atLeastNumeric",
    # Numeric complex password required.
    NumericComplex = "numericComplex",
    # At least alphabetic password required.
    AtLeastAlphabetic = "atLeastAlphabetic",
    # At least alphanumeric password required.
    AtLeastAlphanumeric = "atLeastAlphanumeric",
    # At least alphanumeric with symbols password required.
    AlphanumericWithSymbols = "alphanumericWithSymbols",

