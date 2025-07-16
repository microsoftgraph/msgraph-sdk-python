from enum import Enum

class EndUserNotificationType(str, Enum):
    Unknown = "unknown",
    PositiveReinforcement = "positiveReinforcement",
    NoTraining = "noTraining",
    TrainingAssignment = "trainingAssignment",
    TrainingReminder = "trainingReminder",
    UnknownFutureValue = "unknownFutureValue",

