from enum import Enum

class EndUserNotificationSettingType(str, Enum):
    Unknown = "unknown",
    NoTraining = "noTraining",
    TrainingSelected = "trainingSelected",
    NoNotification = "noNotification",
    UnknownFutureValue = "unknownFutureValue",

