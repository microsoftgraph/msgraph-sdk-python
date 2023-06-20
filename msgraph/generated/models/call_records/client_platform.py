from enum import Enum

class ClientPlatform(str, Enum):
    Unknown = "unknown",
    Windows = "windows",
    MacOS = "macOS",
    IOS = "iOS",
    Android = "android",
    Web = "web",
    IpPhone = "ipPhone",
    RoomSystem = "roomSystem",
    SurfaceHub = "surfaceHub",
    HoloLens = "holoLens",
    UnknownFutureValue = "unknownFutureValue",

