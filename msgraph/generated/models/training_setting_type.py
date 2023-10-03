from enum import Enum

class TrainingSettingType(str, Enum):
    MicrosoftCustom = "microsoftCustom",
    MicrosoftManaged = "microsoftManaged",
    NoTraining = "noTraining",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

