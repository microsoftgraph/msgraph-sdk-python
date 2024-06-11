from enum import Enum

class WindowsAutopilotDeviceType(str, Enum):
    # Default. Indicates that the device type  is a Windows PC.
    WindowsPc = "windowsPc",
    # Indicates that the device type is a HoloLens.
    HoloLens = "holoLens",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

