from enum import Enum

class VolumeType(Enum):
    OperatingSystemVolume = "operatingSystemVolume",
    FixedDataVolume = "fixedDataVolume",
    RemovableDataVolume = "removableDataVolume",
    UnknownFutureValue = "unknownFutureValue",

