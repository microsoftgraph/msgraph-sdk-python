from enum import Enum

class ApplicationType(str, Enum):
    # The windows universal application
    Universal = "universal",
    # The windows desktop application
    Desktop = "desktop",

