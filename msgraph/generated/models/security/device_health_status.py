from enum import Enum

class DeviceHealthStatus(Enum):
    Active = "active",
    Inactive = "inactive",
    ImpairedCommunication = "impairedCommunication",
    NoSensorData = "noSensorData",
    NoSensorDataImpairedCommunication = "noSensorDataImpairedCommunication",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

