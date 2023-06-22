from enum import Enum

class VisibilitySetting(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Hide.
    Hide = "hide",
    # Show.
    Show = "show",

