from enum import Enum

class DiagnosticDataSubmissionMode(str, Enum):
    # Allow the user to set.
    UserDefined = "userDefined",
    # No telemetry data is sent from OS components. Note: This value is only applicable to enterprise and server devices. Using this setting on other devices is equivalent to setting the value of 1.
    None_ = "none",
    # Sends basic telemetry data.
    Basic = "basic",
    # Sends enhanced telemetry data including usage and insights data.
    Enhanced = "enhanced",
    # Sends full telemetry data including diagnostic data, such as system state.
    Full = "full",

