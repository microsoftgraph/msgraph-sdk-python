from enum import Enum

class ExportLocation(str, Enum):
    ResponsiveLocations = "responsiveLocations",
    NonresponsiveLocations = "nonresponsiveLocations",
    UnknownFutureValue = "unknownFutureValue",

