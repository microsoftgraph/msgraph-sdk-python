from enum import Enum

class SynchronizationScheduleState(str, Enum):
    Active = "Active",
    Disabled = "Disabled",
    Paused = "Paused",

