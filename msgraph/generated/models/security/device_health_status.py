from enum import Enum

class DeviceHealthStatus(str, Enum):
    Active = "active",
    Inactive = "inactive",
    ImpairedCommunication = "impairedCommunication",
    NoSensorData = "noSensorData",
    NoSensorDataImpairedCommunication = "noSensorDataImpairedCommunication",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

