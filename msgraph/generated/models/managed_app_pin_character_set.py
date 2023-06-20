from enum import Enum

class ManagedAppPinCharacterSet(str, Enum):
    # Numeric characters
    Numeric = "numeric",
    # Alphanumeric and symbolic characters
    AlphanumericAndSymbol = "alphanumericAndSymbol",

