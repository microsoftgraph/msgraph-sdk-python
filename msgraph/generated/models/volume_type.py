from enum import Enum

class VolumeType(str, Enum):
    OperatingSystemVolume = "operatingSystemVolume",
    FixedDataVolume = "fixedDataVolume",
    RemovableDataVolume = "removableDataVolume",
    UnknownFutureValue = "unknownFutureValue",

