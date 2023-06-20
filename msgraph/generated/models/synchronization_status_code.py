from enum import Enum

class SynchronizationStatusCode(str, Enum):
    NotConfigured = "NotConfigured",
    NotRun = "NotRun",
    Active = "Active",
    Paused = "Paused",
    Quarantine = "Quarantine",

