from enum import Enum

class EventType(Enum):
    SingleInstance = "singleInstance",
    Occurrence = "occurrence",
    Exception = "exception",
    SeriesMaster = "seriesMaster",

