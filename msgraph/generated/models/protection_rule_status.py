from enum import Enum

class ProtectionRuleStatus(str, Enum):
    Draft = "draft",
    Active = "active",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    UnknownFutureValue = "unknownFutureValue",
    UpdateRequested = "updateRequested",
    DeleteRequested = "deleteRequested",

