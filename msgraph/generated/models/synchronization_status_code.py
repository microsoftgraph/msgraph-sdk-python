from enum import Enum

class SynchronizationStatusCode(Enum):
    NotConfigured = "NotConfigured",
    NotRun = "NotRun",
    Active = "Active",
    Paused = "Paused",
    Quarantine = "Quarantine",

